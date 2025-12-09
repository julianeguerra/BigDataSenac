CREATE DATABASE spotify;
USE spotify;

CREATE TABLE spotify_2023 (
    track_name VARCHAR(255),
    artist_name VARCHAR(255),
    artist_count INT,
    released_year INT,
    released_month INT,
    released_day INT,
    in_spotify_playlists INT,
    in_spotify_charts INT,
    streams BIGINT,
    in_apple_playlists INT,
    in_apple_charts INT,
    in_deezer_playlists INT,
    in_deezer_charts INT,
    in_shazam_charts INT,
    bpm INT,
    music_key VARCHAR(5),
    mode VARCHAR(10),
    danceability_percent INT,
    valence_percent INT,
    energy_percent INT,
    acousticness_percent INT,
    instrumentalness_percent INT,
    liveness_percent INT,
    speechiness_percent INT
);

ALTER TABLE spotify_2023 ADD COLUMN track_id INT AUTO_INCREMENT PRIMARY KEY FIRST;

SELECT * FROM spotify_2023;

