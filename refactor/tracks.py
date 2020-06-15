from wsgiref.simple_server import make_server
from db_utils import db_connect


def tracks_table():
    conn = db_connect()
    cur = conn.cursor()

    cur.execute('SELECT Tracks.TrackId, Tracks.Name, Tracks.Composer, Tracks.Milliseconds/1000, albums.Title FROM albums LEFT JOIN Tracks ON Tracks.AlbumId = albums.AlbumId order by Tracks.TrackId asc;')
    rows = cur.fetchall()
    
    cur.execute("SELECT TrackId FROM Tracks")
    IDs = cur.fetchall()
    
    id_num = 0
    countLinks = 0
    
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
                <br>
                <a href="http://127.0.0.1:8000" class="button" style="color:green;padding:15px 32px;text-align:center;font-size:50px;">Home</a>
                <a href="http://127.0.0.1:8000/tracks/"><p style="font-size:38px">Tracks</p></a>
                <br><br>
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

            html += "<td>"

            if count == 2: #Link only in track name
                
                html += """<a href='http://127.0.0.1:8000/tracks/{}'
                              style='color:orange'>""".format(id_num)

            html += str(cell)

            if count == 2:

                html += "</a>"
            html += "</td>"
        html += "</tr>"
    html += "</table></body></html>"

    return html
    

def all_tracks_page(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/html')]

    start_response(status, response_headers)

    html = tracks_table()
    result = html.encode('utf-8')
    
    return [result]