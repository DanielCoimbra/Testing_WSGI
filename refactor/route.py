#! /usr/bin/env python
from wsgiref.simple_server import make_server
from root import root_page
from artists import artists_page
from tracks import all_tracks_page
from track_page import track_page
from schedule import schedule_page
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
from werkzeug.wrappers import Request
from werkzeug.middleware.dispatcher import DispatcherMiddleware

url_map = Map(
    [
        Rule("/", endpoint=root_page),
        Rule("/tracks", endpoint=all_tracks_page),
        Rule("/tracks/<int(min=1, max=3503):TrackId>/", endpoint=track_page),
        Rule("/artists", endpoint=artists_page),
        Rule("/schedule", endpoint=schedule_page)
    ]
)


def route(environ, start_response):
    urls = url_map.bind_to_environ(environ)

    try:
        endpoint, args = urls.match(environ.get("PATH_INFO") or "/")
    except (NotFound, RequestRedirect) as e:
        pass

        return e(environ, start_response)

    return endpoint(environ, start_response)
