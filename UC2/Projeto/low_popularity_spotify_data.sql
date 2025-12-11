CREATE DATABASE spotify;
USE spotify;

CREATE TABLE low_popularity_spotify_data (
    time_signature INT,
    track_popularity INT,
    speechiness FLOAT,
    danceability FLOAT,
    playlist_name VARCHAR(255),
    track_artist VARCHAR(255),
    duration_ms INT,
    energy INT,
    playlist_genre VARCHAR(50),
    playlist_subgenre VARCHAR(50),
    track_href VARCHAR(255),
    track_name VARCHAR(255),
    music_mode INT,
    uri VARCHAR(255),
    music_type VARCHAR(50),
    track_album_release_date VARCHAR(100),
    analysis_url VARCHAR(255),
    id VARCHAR(255)  PRIMARY KEY,
    instrumentalness DECIMAL,
    track_album_id VARCHAR(255),
    playlist_id VARCHAR(255),
    track_id VARCHAR(255),
    valence FLOAT,
    music_key INT,
    tempo FLOAT,
    loudness FLOAT,
    acousticness DECIMAL,
    liveness FLOAT,
    track_album_name VARCHAR(255)
);

SET SESSION sql_mode = '';

LOAD DATA LOCAL INFILE "C:/Users/juliane.guerra/OneDrive - SENAC RIO/Documentos/BigDataSenac/UC2/Projeto/low_popularity_spotify_data.csv" -- Ajuste o caminho no seu banco local
INTO TABLE spotify.low_popularity_spotify_data
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(time_signature,track_popularity,speechiness,danceability,playlist_name,track_artist,duration_ms,energy,playlist_genre,playlist_subgenre,track_href,track_name,music_mode,uri,music_type,track_album_release_date,analysis_url,id,instrumentalness,track_album_id,playlist_id,track_id,valence,music_key,tempo,loudness,acousticness,liveness,track_album_name); -- Mapeia colunas

SELECT * FROM low_popularity_spotify_data;

SELECT COUNT(*) FROM low_popularity_spotify_data;