SELECT username, email, bio FROM app_user LIMIT 20;

SELECT name FROM tag LIMIT 20;

SELECT name FROM ingredient LIMIT 20;

SELECT 
     r.title,
     r.description, 
     r.created_at,
     STRING_AGG(i.name, ', ') AS ingredients 
FROM recipe_ingredient ri
JOIN ingredient i ON i.name = ri.ingredient_name
JOIN recipe r ON r.id = ri.recipe_id
GROUP BY r.id
LIMIT 20;

SELECT
     r.title,
     s.description,
     s.number
FROM recipe r
JOIN steps s ON s.recipe_id = r.id
LIMIT 20;

SELECT table_name, action FROM logger LIMIT 50;

