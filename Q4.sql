drop database if exists foundation_assessment_ii;
CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

CREATE TABLE movie_info (
    Movie_ID int NOT NULL,
    Movie_Name VARCHAR(20) NOT NULL,
    Movie_Length VARCHAR(20) NOT NULL,
    Age_Rating VARCHAR(20) NOT NULL
); 

CREATE TABLE screens (
    Screen_ID int NOT NULL,
    Four_K Boolean NOT NULL
); 

CREATE TABLE showings (
    Showing_ID int NOT NULL,
    Movie_ID int NOT NULL,
    Screen_ID int NOT NULL,
    Start_Time VARCHAR(20) NOT NULL,
    Available_Seats int NOT NULL
); 