from wsgiref.simple_server import make_server
from db_utils import db_connect, get_artists
from werkzeug.wrappers import Request, Response
import pystache

    
@Request.application
def artists_page(request):
    
    with open("templates/artists.html") as template:
        html = pystache.render(template.read(), get_artists())

    
    
    return Response([html], status=200, mimetype='text/html')