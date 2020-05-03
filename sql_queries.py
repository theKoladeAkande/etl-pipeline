#Fact Table
CREATE_SONGPLAYS_TABLE = """ CREATE TABLE IF NOT EXISTS  songplays
                            ( songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
                            start_time TIMESTAMP,
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
                              week INT NOT NULL,
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
                           VALUES(%s, %s, %s, %s, %s)
                           ON CONFLICT (artist_id) DO UPDATE SET
                          location = EXCLUDED.location,
                          latitude = EXCLUDED.latitude,
                          longitude = EXCLUDED.longitude"""

USERS_TABLE_INSERT = """ INSERT INTO users (user_id, first_name, last_name, gender, level)
                         VALUES(%s, %s, %s, %s, %s)
                         ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;"""

TIME_TABLE_INSERT = """ INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        VALUES(to_timestamp(%s), %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (start_time) DO NOTHING"""

SONGPLAYS_TABLE_INSERT = """INSERT INTO songplays(
                          start_time,
                          user_id,
                          level,
                          song_id,
                          artist_id,
                          session_id,
                          location,
                          user_agent)
                          VALUES (to_timestamp(%s),%s,%s,%s,%s,%s,%s,%s)"""

#select
SONG_SELECT = """SELECT songs.song_id , artists.artist_id FROM songs JOIN artists
              ON songs.artist_id = artists.artist_id
              where title=%s AND name=%s AND duration=%s;"""



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