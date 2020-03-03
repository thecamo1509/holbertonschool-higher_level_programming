-- script that will list all cities in a DB --
SELECT cities.id, cities.name, states.name 
FROM cities
INNER JOIN states ON cities.state_id=states.id;
