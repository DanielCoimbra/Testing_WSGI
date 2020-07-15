import pystache
from wsgiref.simple_server import make_server
from werkzeug.wrappers import BaseRequest as Request, Response

@Request.application
def root_page(request):
    
    with open("templates/root.html.mustache") as template:
        html = pystache.render(template.read())

    return Response([html], status=200, mimetype='text/html')