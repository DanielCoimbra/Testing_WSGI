from wsgiref.simple_server import make_server
from db_utils import db_connect, get_all_tracks
from werkzeug.wrappers import Request, Response
import pystache


@Request.application
def all_tracks_page(request):

    with open("templates/all_tracks.html") as template:
        html = pystache.render(
            template.read(), {"rows": [r._asdict() for r in get_all_tracks()]}
        )

    return Response([html], status=200, mimetype="text/html")
