-- script that will list of the cities in the DB --
SELECT id, name 
FROM cities 
WHERE state_id =(
    SELECT id
    FROM states
    WHERE name = 'California'
);