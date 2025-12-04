CREATE DATABASE spotify;
USE spotify;

CREATE TABLE track_data_final (
track_id VARCHAR(255) PRIMARY KEY,
track_name VARCHAR(255),
track_number INT,
track_popularity INT,
track_duration_ms INT,
explicit VARCHAR(255),
artist_name VARCHAR(255),
artist_popularity INT,
artist_followers INT,
artist_genres VARCHAR(50),
album_id VARCHAR(255),
album_name VARCHAR(255),
album_release_date DATE,
album_total_tracks INT,
album_type VARCHAR(50)
);

SELECT * FROM track_data_final;

