-- a script that lists all genres from hbtn_0d_tvshows with its count
SELECT tv_gen.name as genre, COUNT(show_gen.show_id) as number_of_shows
FROM tv_genres as tv_gen
INNER JOIN tv_show_genres as show_gen
ON tv_gen.id = show_gen.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
