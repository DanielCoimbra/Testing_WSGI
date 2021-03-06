#! /usr/bin/python3
from db_utils import db_connect
# All tracks               CHECK
# Artists                  CHECK
# Track_Page


def template(Title, Body):
    html = """
        <!DOCTYPE HTML>
        <head>
            <title>Music Store</title>
            <!-- CSS only -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

            <!-- JS, Popper.js, and jQuery -->
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
        </head>
        <html>
            <body>        
                <p style="font-size:90px;text-align:center">Music Store</p>
                <p style="padding-left:30px;font-size:60px">{}</p>
                <a href="http://127.0.0.1:8000" class="button" style="color:green;padding:15px 32px;text-align:center;font-size:50px;">Home</a>
                <br>
                <br>
                <br>
                <br>
                {}
            </body>
        </html>""".format(Title, Body)

    return html.encode('utf-8')


def all_tracks():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT Tracks.TrackId, Tracks.Name, Tracks.Composer, Tracks.Milliseconds/1000, albums.Title FROM albums LEFT JOIN Tracks ON Tracks.AlbumId = albums.AlbumId order by Tracks.TrackId asc;')
    rows = cur.fetchall()
    cur.execute("SELECT TrackId FROM Tracks")
    IDs = cur.fetchall()
    id_num = 0
    countLinks = 0
    html = """
    
        <table class="table table-striped">
            <tr>
                <th>TrackID</th>
                <th>Name</th>
                <th>Composer</th>
                <th>Seconds</th>
                <th>Album</th>
            </tr>
            """

    for row in rows:
        id_num += 1
        count = 0
        html += """<tr>"""

        for cell in row:
            count += 1

            html += "<td style='color:green;'>"  # Open cell tag

            if count == 2:  # this makes sure only the Name has a bound link
                # Open Link tag
                html += "<a href='http://127.0.0.1:8000/tracks/{}' style='color:orange'>".format(
                    id_num)

            html += str(cell)  # Table Cell Argument

            if count == 2:  # this makes sure only the Name has a bound link

                html += "</a>"  # close link tag
            html += "</td>"  # Close cell tag
        html += "</tr>"
    html += "</table>"

    return html


def artists_page():

    conn = db_connect()
    cur = conn.cursor()
    cur.execute(
        'SELECT artists.Name, albums.Title FROM artists LEFT JOIN albums ORDER BY artists.Name')
    rows = cur.fetchall()
    html = """
        <table>
            <tr> <th>Artist</th><th>Album</th> </tr>"""
    for row in rows:
        html += "<tr> <td>{}</td> <td>{}</td> </tr>".format(row[0], row[1])
    html += "</table>"
    return html


def track_page(TrackId):
    conn = db_connect()
    cur = conn.cursor()
    sql = "SELECT Name, Composer FROM Tracks WHERE TrackId=?"
    cur.execute(sql, TrackId)
    rows = cur.fetchall()
    for x, y in rows:
        name = x
        composer = y

    html = """
    
    <form method="post" action="">
        <label for="Track">Track:</label>
        <input style="width:80%" "type="text" id="Track" name="Track" value ="{}" required>
        <br>
        <br>
        <label for="Composer">Composer:</label>
        <input style="width:80%" type="text" id="Composer" name="Composer" value ="{}" required>
        <br>
        <br>
        <input type="submit" value="Submit">
    </form>
    
    <a href="http://127.0.0.1:8000" class="button" style="color:red;padding:10px 10px;text-align:center;font-size:35px;">Cancel</a>
    """.format(name, composer)
    return html


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
