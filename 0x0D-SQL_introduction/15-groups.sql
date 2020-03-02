-- script that shows the number of records of equal scores --
SELECT 
    score, 
    COUNT(score) as number
FROM
    second_table
GROUP BY score
ORDER BY score DESC
HAVING COUNT(score) >= 1;