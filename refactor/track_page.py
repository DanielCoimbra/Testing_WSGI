from db_utils import db_connect, track_form_handler, get_single_track
from cgi import escape, parse_qs
from wsgiref.simple_server import make_server
from werkzeug.wrappers import Request, Response
import pystache

def post_request(environ):
    path = environ["PATH_INFO"]
    path_sections = path.split("/")

    try:
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ["wsgi.input"].read(request_body_size)
    d = parse_qs(request_body)
    track = d[b"Track"]
    composer = d[b"Composer"]
    track = str(track)
    track = escape(track)
    composer = str(composer)
    composer = escape(composer)
    track_form_handler(
        path_sections[2], track[3 : len(track) - 2], composer[3 : len(composer) - 2]
    )


def track_page_form(TrackId):  # GET method
    conn = db_connect()
    cur = conn.cursor()
    sql = "SELECT Name, Composer FROM Tracks WHERE TrackId=?"
    cur.execute(sql, TrackId)
    rows = cur.fetchall()
    cur.close()
    conn.close()


    for x, y in rows:
        name = x
        composer = y
        form = """
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
            </form>""".format(
            name, composer
        )
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
            {}
            <a href="http://127.0.0.1:8000/tracks" class="button" style="color:red;padding:10px 10px;text-align:center;font-size:35px;">Cancel</a>
        </body>
    </html>
    """.format(
        form
    )

    return html


@Request.application
def track_page(request):
    if request.method == "GET":

        path = request.environ["PATH_INFO"]
        path_sections = path.split("/")
        track_id = path_sections[2]
        

        with open("templates/single_track.html") as template:
            html = pystache.render(template.read(), get_single_track(track_id))

        return Response([html], mimetype="text/html")


    elif request.method == "POST":
        post_request(request.environ)

        result = tracks_table()

        return Response(
            [result],
            status=302,
            mimetype="text/html",
            headers={"Location": "http://localhost:8000/tracks"},
        )

