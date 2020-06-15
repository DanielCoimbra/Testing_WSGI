import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'music_store.db')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)

    return con
    

def track_form_handler(TrackId, name, comp):
    conn = db_connect()
    cur = conn.cursor()

    sql = "UPDATE Tracks SET Name = ?, Composer = ? WHERE TrackId = ?"

    try:
        cur.execute(sql, (name, comp, TrackId))
        conn.commit()
    except:
        conn.rollback()

        raise RuntimeError("An error occurred...")
