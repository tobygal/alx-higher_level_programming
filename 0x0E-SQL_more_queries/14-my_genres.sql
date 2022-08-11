-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_gen.name as name
FROM tv_genres as tv_gen
JOIN tv_show_genres as show_gen
ON tv_gen.id = show_gen.genre_id
JOIN tv_shows as shows
ON shows.id = show_gen.show_id
WHERE shows.title = "Dexter"
ORDER BY name ASC;
