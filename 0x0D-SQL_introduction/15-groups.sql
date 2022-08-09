-- list count of each record
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score;
