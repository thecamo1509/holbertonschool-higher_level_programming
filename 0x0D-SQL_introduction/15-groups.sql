-- script that shows the number of records of equal scores --
SELECT score, COUNT(score) FROM second_table ORDER BY score DESC GROUP BY score HAVING COUNT(score) > 1;