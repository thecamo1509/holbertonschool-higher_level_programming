-- script that uses the DB to show genres of Dexter --
SELECT name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.show_id = 8 
AND tv_show_genres.genre_id = tv_genres.id
;