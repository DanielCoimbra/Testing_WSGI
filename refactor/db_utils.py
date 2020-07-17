import os
import sqlite3
from collections import namedtuple

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "music_store.db")


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
        conn.close()
    except:
        conn.rollback()

        raise RuntimeError("An error occurred...")


def get_artists():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT albums.Title, artists.Name FROM albums
    LEFT JOIN artists ON albums.ArtistId = artists.ArtistID"""
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    artists_dict = {"items": []}

    for row in rows:
        dictionary = {}
        try:
            dictionary["artist"] = str(row[0])
        except Exception:
            dictionary["artist"] = "None"
        try:
            dictionary["album"] = str(row[1])
        except Exception:
            dictionary["album"] = "None"
        artists_dict["items"].append(dictionary)

    return artists_dict


Track = namedtuple("Track", ["TrackId", "Name", "Composer", "Milliseconds", "Album"])
# t = Track(1, "SDASDFASDF", "Fulano")
# t.Name
# t[1]
# for field in t:
#     print field
# t._asdict() -> {"TrackId": 1, "Name": "ASDASDAS", "Composer": "fulano"}


def get_all_tracks():
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT Tracks.TrackId, Tracks.Name, Tracks.Composer, Tracks.Milliseconds/1000, albums.Title FROM albums LEFT JOIN Tracks ON Tracks.AlbumId = albums.AlbumId order by Tracks.TrackId asc;"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [Track(*row) for row in rows]

    # all_tracks_dict = {"rows": []}

    # for row in rows:
    #     dictionary = {}
    #     try:
    #         dictionary["TrackId"] = str(row[0])
    #     except Exception:
    #         dictionary["TrackId"] = "None"
    #     try:
    #         dictionary["Name"] = str(row[1])
    #     except Exception:
    #         dictionary["Name"] = "None"
    #     try:
    #         dictionary["Composer"] = str(row[2])
    #     except Exception:
    #         dictionary["Composer"] = "None"

    #     try:
    #         dictionary["Milliseconds"] = str(row[3])
    #     except Exception:
    #         dictionary["Milliseconds"] = "None"

    #     try:
    #         dictionary["Album"] = str(row[4])
    #     except Exception:
    #         dictionary["Album"] = "None"

    #     all_tracks_dict["rows"].append(dictionary)

    # return all_tracks_dict


def get_single_track(TrackId):
    conn = db_connect()
    cur = conn.cursor()
    sql = "SELECT Name, Composer FROM Tracks WHERE TrackId=?"
    cur.execute(sql, TrackId)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    track_dict = {"item": [{"Name": None, "Composer": None}]}

    try:
        track_dict["item"][0]["Name"] = rows[0][0]
    except Exception:
        track_dict["item"][0]["Name"] = "None"

    try:
        track_dict["item"][0]["Composer"] = rows[0][1]
    except Exception:
        track_dict["item"][0]["Composer"] = "None"

    return track_dict
