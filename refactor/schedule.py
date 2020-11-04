from wsgiref.simple_server import make_server
from db_utils import db_connect, get_all_tracks
from werkzeug.wrappers import Request, Response
import pystache


@Request.application
def schedule_page(request):

    with open("templates/schedule.html") as template:
        html = pystache.render(
            template.read(), {"rows": [r._asdict() for r in get_all_tracks()]}
        )

    return Response([html], status=200, mimetype="text/html")
 

"""
 I'll have to create a schedule for events in the eventmaster project. 
 The model for this schedule is https://win.iweventos.com.br/evento/avc2019/programacao/gradeatividades/23

 Don't forget to use bootstrap and if there is enough time to try out switchstrap or bootswitch, bootswatch somethin' like that

 Also, for future projects, learn to use SQL and migrate the whole db_utils from this project to the SLQAlchemy architechture
 
"""