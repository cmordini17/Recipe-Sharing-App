# script for writing sql queries based on recipe and user csv files.
# uuids must be defined in your csv files. They must be this format: '00000000-0000-0000-0000-000000000000' where each zero is a valid hex value.
import csv

user_queries = ""
recipe_queries = ""
tag_queries = ""
ingredient_queries = "" 
steps_queries = ""
recipe_ingredient_queries = ""
recipe_tag_queries = ""

with open("users.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for id, username, email, pw_hash, bio in reader:
        user_queries += (
            "INSERT INTO app_user (id, username, email, password_hash, bio) "
            f"VALUES ('{id}', '{username}', '{email}', '{pw_hash}', '{bio}');\n"
        )

with open("recipes.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for  id, user_id, title, description, ingredients, tags, steps in reader:
        ingredients_list = ingredients.strip().split(";")
        tags_list = tags.strip().split(";")
        steps_list = steps.strip().split(";")
        recipe_queries += (
            "INSERT INTO recipe (id, user_id, title, description) "
            f"VALUES ('{id}', '{user_id}', '{title}', '{description}');\n"
        )

        for ingredient in ingredients_list:
            ingredient_queries += (
                f"INSERT INTO ingredient (name) VALUES ('{ingredient}')"
                " ON CONFLICT (name) DO NOTHING;\n"
            )
            recipe_ingredient_queries += (
                f"INSERT INTO recipe_ingredient (recipe_id, ingredient_name) "
                f"VALUES ('{id}', '{ingredient}');\n"
            )

        for tag in tags_list:
            tag_queries += (
                f"INSERT INTO tag (name) VALUES ('{tag}') "
                "ON CONFLICT (name) DO NOTHING;\n"
            )
            recipe_tag_queries += (
                "INSERT INTO recipe_tag (recipe_id, tag_name) "
                f"VALUES ('{id}', '{tag}');\n"
            )

        for index, step in enumerate(steps_list, start=1):
            steps_queries += (
                "INSERT INTO steps (recipe_id, number, description) "
                f"VALUES ('{id}', {index}, '{step}');\n"
            )

with open("sql/load_test_data.sql", "w") as file:
    file.write(user_queries)
    file.write(recipe_queries)
    file.write(ingredient_queries)
    file.write(recipe_ingredient_queries)
    file.write(tag_queries)
    file.write(recipe_tag_queries)
    file.write(steps_queries)