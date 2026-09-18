DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS recipe;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS follows;
DROP TABLE IF EXISTS steps;
DROP TABLE IF EXISTS recipe_tag;
DROP TABLE IF EXISTS recipe_ingredient;
DROP TABLE IF EXISTS recipe_like;
DROP TABLE IF EXISTS logger;

CREATE TABLE user (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password_hash TEXT NOT NULL,
    name VARCHAR(255),
    bio TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE recipe (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE tag (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE ingredient (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE steps (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    number INT NOT NULL,
    text TEXT NOT NULL,
    PRIMARY KEY (recipe_id, number)
);

CREATE TABLE recipe_ingredient (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    ingredient_id UUID NOT NULL REFERENCES ingredient(id) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, ingredient_id)
);

CREATE TABLE recipe_tag (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    tag_id UUID NOT NULL REFERENCES tag(id) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, tag_id)
);

CREATE TABLE recipe_like (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (recipe_id, user_id)
);