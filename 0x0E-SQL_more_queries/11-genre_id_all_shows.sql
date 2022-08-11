-- a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT shows.title, show_gen.genre_id
FROM tv_shows as shows
LEFT OUTER JOIN tv_show_genres as show_gen
ON shows.id = show_gen.show_id
ORDER BY shows.title, show_gen.genre_id;
