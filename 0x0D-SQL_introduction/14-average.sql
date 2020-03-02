-- finding the score from the scores --
INSERT INTO second_table (average)
VALUES (SELECT AVG(score) FROM second_table);