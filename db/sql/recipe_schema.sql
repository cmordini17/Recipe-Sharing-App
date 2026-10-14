DROP TABLE IF EXISTS follows;
DROP TABLE IF EXISTS steps;
DROP TABLE IF EXISTS recipe_tag;
DROP TABLE IF EXISTS recipe_ingredient;
DROP TABLE IF EXISTS recipe_like;
DROP TABLE IF EXISTS logger;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS recipe;
DROP TABLE IF EXISTS app_user;

CREATE TABLE app_user (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password_hash TEXT NOT NULL,
    bio TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE recipe (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES app_user(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE tag (
    name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE ingredient (
    name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE step (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    number INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (recipe_id, number)
);

CREATE TABLE recipe_ingredient (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    ingredient_name VARCHAR(255) NOT NULL REFERENCES ingredient(name) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, ingredient_name)
);

CREATE TABLE recipe_tag (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    tag_name VARCHAR(255) NOT NULL REFERENCES tag(name) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, tag_name)
);

CREATE TABLE recipe_like (
    recipe_id UUID NOT NULL REFERENCES recipe(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES app_user(id) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (recipe_id, user_id)
);

CREATE TABLE logger (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID,
    table_name VARCHAR(255) NOT NULL,
    action VARCHAR(255) NOT NULL,
    log_time TIMESTAMP DEFAULT NOW()
)
