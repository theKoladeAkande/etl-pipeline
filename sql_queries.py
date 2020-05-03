#Fact Table
CREATE_SONGPLAYS_TABLE = """ CREATE TABLE IF NOT EXISTS  songplays
                            ( songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
                            start_time TIMESTAMP ,
                            user_id INT,
                           level VARCHAR NOT NULL,
                            song_id VARCHAR,
                           artist_id VARCHAR,
                            session_id INT NOT NULL,
                            location VARCHAR,
                            user_agent TEXT ); """

#Dimension Table
CREATE_USERS_TABLE = """ CREATE TABLE IF NOT EXISTS  users
                            ( user_id  INT CONSTRAINT users_pk PRIMARY KEY,
                            first_name VARCHAR,
                            last_name VARCHAR,
                            gender CHAR(1),
                            level VARCHAR NOT NULL); """

CREATE_SONGS_TABLE = """ CREATE TABLE IF NOT EXISTS  songs
                            ( song_id VARCHAR CONSTRAINT songs_pk PRIMARY KEY,
                            title VARCHAR,
                            artist_id VARCHAR,
                            year INT,
                            duration FLOAT); """

CREATE_ARTISTS_TABLE = """ CREATE TABLE IF NOT EXISTS  artists
                            ( artist_id VARCHAR CONSTRAINT artist_pk PRIMARY KEY,
                            name VARCHAR,
                            location VARCHAR,
                            latitude FLOAT,
                            longitude FLOAT); """

CREATE_TIME_TABLE = """ CREATE TABLE IF NOT EXISTS  time
                            ( start_time TIMESTAMP CONSTRAINT time_pk PRIMARY KEY,
                              hour INT NOT NULL,
                              day INT NOT NULL,
                              month INT NOT NULL,
                              year INT NOT NULL,
                              weekday INT NOT NULL); """

DROP_SONGPLAYS_TABLE = """ DROP table if exists songplays"""
DROP_USERS_TABLE = """ DROP table  if exists users """
DROP_SONGS_TABLE = """ DROP table if exists songs """
DROP_ARTISTS_TABLE = """ DROP table if exists artists """
DROP_TIME_TABLE = """ DROP table if exists time """

#insert
SONGS_TABLE_INSERT = """ INSERT INTO songs (song_id, title, artist_id, year, duration )
                         VALUES(%s, %s, %s, %s, %s) """

ARTISTS_TABLE_INSERT = """ INSERT INTO artists (artist_id, name, location, latitude, longitude)
                           VALUES(%s, %s, %s, %s, %s)"""

USERS_TABLE_INSERT = """ INSERT INTO users (user_id, first_name, last_name, gender, level)
                         VALUES(%s, %s, %s, %s, %s)"""

TIME_TABLE_INSERT = """ INSERT INTO table (start_time, hour, day, month, year, weekday)
                        VALUES(%s, %s, %s, %s, %s, %s)"""



DROP_QUERIES = [DROP_SONGPLAYS_TABLE,
               DROP_ARTISTS_TABLE,
               DROP_USERS_TABLE,
               DROP_SONGS_TABLE,
               DROP_TIME_TABLE]

CREATE_QUERIES = [CREATE_SONGPLAYS_TABLE,
                 CREATE_ARTISTS_TABLE,
                 CREATE_SONGS_TABLE,
                 CREATE_USERS_TABLE,
                 CREATE_TIME_TABLE]