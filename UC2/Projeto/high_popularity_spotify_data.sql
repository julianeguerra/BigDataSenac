CREATE DATABASE spotify;
USE spotify;
SET SESSION sql_mode = '';


CREATE TABLE high_popularity_spotify_data (
    energy INT,
    tempo FLOAT,
    danceability FLOAT,
    playlist_genre VARCHAR(50),
    loudness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    track_artist TEXT,
    time_signature INT,
    speechiness FLOAT,
    track_popularity INT,
    track_href VARCHAR(500),
    uri VARCHAR(500),
    track_album_name VARCHAR(500),
    playlist_name VARCHAR(500),
    analysis_url VARCHAR(500),
    track_id VARCHAR(255),
    track_name VARCHAR(500),
    track_album_release_date VARCHAR(100),
    instrumentalness DECIMAL,
    track_album_id VARCHAR(255),
    music_mode INT,
    music_key INT,
    duration_ms INT,
    acousticness DECIMAL,
    id VARCHAR(255) PRIMARY KEY,
    playlist_subgenre VARCHAR(100),
    music_type VARCHAR(100),
    playlist_id VARCHAR(255)
);

DESCRIBE high_popularity_spotify_data;

LOAD DATA LOCAL INFILE "C:/Users/juliane.guerra/OneDrive - SENAC RIO/Documentos/BigDataSenac/UC2/Projeto/high_popularity_spotify_data.csv" -- Ajuste o caminho no seu banco local
INTO TABLE spotify.high_popularity_spotify_data
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(energy,tempo,danceability,playlist_genre,loudness,liveness,valence,track_artist,time_signature,speechiness,track_popularity,track_href,uri,track_album_name,playlist_name,analysis_url,track_id,track_name,track_album_release_date,instrumentalness,track_album_id,music_mode,music_key,duration_ms,acousticness,id,playlist_subgenre,music_type,playlist_id); -- Mapeia colunas

SELECT * FROM high_popularity_spotify_data;

SELECT COUNT(*) FROM high_popularity_spotify_data;

