#! /usr/bin/env python
from wsgiref.simple_server import make_server
from root import root_page
from artists import artists_page
from tracks import all_tracks_page
from track_page import track_page

from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect


def application(environ, start_response):
    environ = environ
    urls = Map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match(environ.get('PATH_INFO') or '/')
    except (NotFound, RequestRedirect) as  e:
        return e(environ, start_response)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Rule points to %r with arguments %r' % (endpoint, args)]


def dispatch_request(request):

    adapter = self.url_map.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        return getattr(self, f"on_{endpoint}")(request, **values)
    except NotFound:
        return self.error_404()
    except HTTPException as e:
        return e


def wsgi_app(environ, start_response):
    request = Request(environ)
    response = dispatch_request(request)

    return response(environ, start_response)


map = Map([
    Rule('/', endpoint='root_page(environ, start_response)'),
    Rule('/tracks', endpoint='all_tracks_page(environ, start_response)'),
    Rule('/tracks/<int(min=1, max=3503):TrackId>/', endpoint='track_page(environ, start_response)'),
    Rule('/artists', endpoint='artists_page(environ, start_response)')
])

def route2(environ, start_response):
    urls = map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match(environ.get('PATH_INFO') or '/')
    except (NotFound, RequestRedirect) as e:
        return e(environ, start_response)
    
    return exec(
                endpoint, globals(),locals() )
                # {
                # "root_page": root.root_page,
                # "all_tracks_page": tracks.all_tracks_page,
                # "track_page": track_page.track_page,
                # "artists_page": artists.artists_page
                # }
                

def route(environ, start_response):
    path = environ['PATH_INFO']
    path_sections = path.split('/')

    if path == "/" or path == '':
    
        return root_page(environ, start_response)
    
    elif path_sections[1] == 'tracks':
        if len(path_sections) > 2 :
            if path_sections[2]=='' or path_sections[2]=='/':
    
                return all_tracks_page(environ, start_response)
            
            elif int(path_sections[2])>=1 and int(path_sections[2])<3503:
                
                return track_page(environ, start_response)
            
            else: 
                
                return error_page(environ, start_response)
        else: 
            
            return all_tracks_page(environ, start_response)
    
    elif path_sections[1] == 'artists':
        
        return artists_page(environ,start_response)
    else:
    
        return error_page(environ, start_response)
    



if __name__ == '__main__':
    from werkzeug.serving import run_simple

    app = route
    run_simple('localhost', 8000, route2, use_reloader=True)


