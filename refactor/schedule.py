from wsgiref.simple_server import make_server
from db_utils import db_connect, get_artists
from werkzeug.wrappers import Request, Response
import pystache
from numpy import array_split

@Request.application
def schedule_page(request):

    with open("templates/schedule.html") as template:
        listt = [r._asdict() for r in get_artists()]
        lis1, lis2, lis3 = array_split(listt, 3)
        dic= {"day1": list(lis1), "day2": list(lis2), "day3": list(lis3)}

        html = pystache.render(
            template.read(), dic
            )

    return Response([html], status=200, mimetype="text/html")
 

"""
 I'll have to create a schedule for events in the eventmaster project. 
 The model for this schedule is https://win.iweventos.com.br/evento/avc2019/programacao/gradeatividades/23

 Don't forget to use bootstrap and if there is enough time to try out switchstrap or bootswitch, bootswatch somethin' like that

 Also, for future projects, learn to use SQL and migrate the whole db_utils from this project to the SLQAlchemy architechture
 
"""