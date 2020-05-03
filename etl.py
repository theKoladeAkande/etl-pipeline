import os
import glob
import pandas as pd
import psycopg2

from connection_manger import dbconnection_manager
import sql_queries

def process_song_file(cursor, filepath):
    """
    Extracts needed information from given song file and inserts
    them to the song and artist PostgreSQL database tables.
    @type cursor: Cursor object
    @param cursor: Cursor connected to PostgreSQL
    @type filepath: string
    @param filepath: Path to song file
    """
    #load songs json file
    df = pd.read_json(filepath, lines=True)
    #extract song data
    song_data = df[['song_id', 'title', 'artist_id','year', 'duration']].values[0].tolist()
    #insert into database
    cursor.execute(sql_queries.SONGS_TABLE_INSERT, song_data)

    #extract artist data
    artist_data = df[['artist_id','artist_name', 'artist_location', \
        'artist_latitude', 'artist_longitude']].values[0].tolist()
        #insert into database
    cursor.execute(sql_queries.ARTISTS_TABLE_INSERT, artist_data)


def process_log_file(cursor, filepath):
    """
    Extracts needed information from given log file and inserts them to the songplay PostgreSQL database table
    @type cursor: Cursor object
    @param cursor: Cursor connected to PostgreSQL
    @type filepath: string
    @param filepath: Path to log file
    """
    #load log json file
    df = pd.read_json(filepath, lines=True)
    #filter NextSong
    df = df[df['page'] == 'NextSong']
    #convert timestamp to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    #extract data
    time_data = (t.apply(lambda x: x.timestamp()).tolist(),
                t.apply(lambda x: x.hour).tolist(),
                t.apply(lambda x: x.day).tolist(),
                t.apply(lambda x: x.weekofyear).tolist(),
                t.apply(lambda x: x.month).tolist(),
                t.apply(lambda x: x.year).tolist(),
                t.apply(lambda x: x.weekday()).tolist() )
    column_labels = ('timestamp', 'hour', 'day', 'weekofyear', 'month', 'year', 'weekday')
    data = {k:v for k,v in zip(column_labels, time_data)}
    time_df = pd.DataFrame.from_dict(data)
    for i, row in time_df.iterrows():
        cursor.execute(sql_queries.TIME_TABLE_INSERT, list(row))


    #extract users data
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    for i, row in user_df.iterrows():
            cursor.execute(sql_queries.USERS_TABLE_INSERT, list(row))


    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cursor.execute(sql_queries.SONG_SELECT, (row.song, row.artist, row.length))
        results = cursor.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

    # insert songplay record
    songplay_data = (row.ts, row.userId, row.level,songid, artistid, row.sessionId, row.location, row.userAgent)
    cursor.execute(sql_queries.SONGPLAYS_TABLE_INSERT, songplay_data)


def process_data(cursor, conn, filepath, func):
    """
    Processes all data from a given filepath with a given function
    @type cursor: Cursor object
    @param cursor: Cursor connected to PostgreSQL
    @type conn: Connection object
    @param conn: Holding the session to the PostgreSQL database
    @type filepath: String
    @param filepath: Path containing subfolders with data that will be crawled in this function
     @type func: Function
    @param func: Function for processing the data inside the given filepath
    """

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print(f'{num_files} files found in {filepath}')

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cursor, datafile)
        conn.commit()
        print(f'{i}/{num_files} files processed.')

def main():
    with dbconnection_manager(dbname="sparkifydb") as (cursor, conn):

            process_data(cursor, conn, filepath='/home/kolade/repos/Sparkify-Etl/data/song_data',
                        func=process_song_file)
            process_data(cursor, conn, filepath='/home/kolade/repos/Sparkify-Etl/data/log_data',
                        func=process_log_file)



if __name__ == "__main__":
    main()