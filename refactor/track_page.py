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
    track, composer = escape(str(d[b"Track"])), escape(str(d[b"Composer"]))

    track_form_handler(
        path_sections[2], track[2 : len(track) - 2], composer[2 : len(composer) - 2]
    )



@Request.application
def track_page(request):

    path = request.environ["PATH_INFO"]
    path_sections = path.split("/")
    track_id = path_sections[2]


    if request.method == "GET":
        with open("templates/single_track.html") as template:
            html = pystache.render(template.read(), get_single_track(track_id))

        return Response(
            [html],
            mimetype="text/html"
            )


    elif request.method == "POST":
        post_request(request.environ)

        with open("templates/all_tracks.html") as template:
            html = pystache.render(template.read(), get_single_track(track_id))

        return Response(
            [html],
            status=302,
            mimetype="text/html",
            headers={"Location": "http://localhost:8000/tracks"},
        )

