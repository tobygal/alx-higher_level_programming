-- list all records of second_table
SELECT score, name
FROM second_table
WHERE name is not NULL
ORDER BY score DESC;
