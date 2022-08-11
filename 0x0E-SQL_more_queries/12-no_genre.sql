-- list all shows without a genre
SELECT shows.title, show_gen.genre_id
FROM tv_shows as shows
LEFT OUTER JOIN tv_show_genres as show_gen
ON shows.id = show_gen.show_id
WHERE show_gen.genre_id IS NULL
ORDER BY shows.title, show_gen.genre_id;
