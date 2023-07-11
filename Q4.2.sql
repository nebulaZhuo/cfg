SELECT movie_info.Movie_Name, showings.Start_Time
FROM movie_info
JOIN showings ON movie_info.Movie_ID = showings.Movie_ID
WHERE showings.Start_Time > '12:00' AND showings.Available_Seats > 0
ORDER BY showings.Start_Time;