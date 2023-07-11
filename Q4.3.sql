SELECT movie_info.Movie_Name
FROM movie_info
JOIN showings ON movie_info.Movie_ID = showings.Movie_ID
GROUP BY movie_info.Movie_Name
ORDER BY COUNT(*) DESC
LIMIT 1;