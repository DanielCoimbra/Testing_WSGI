#! /usr/bin/env python
from wsgiref.simple_server import make_server
from root import root_page
from artists import artists_page
from tracks import all_tracks_page
from track_page import track_form_handler, track_page_form, track_page
from error import error_page
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect


def route2(environ, start_response):
    urls = map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match(environ.get('PATH_INFO') or '/')
    except (NotFound, RequestRedirect) as e:
        return e(environ, start_response)
    
    return exec(
                endpoint, globals(),locals() 
                # {
                # "root_page": root.root_page,
                # "all_tracks_page": tracks.all_tracks_page,
                # "track_page": track_page.track_page,
                # "artists_page": artists.artists_page
                # }
                )


def route(environ, start_response):
    path = environ['PATH_INFO']
    path_sections = path.split('/')

    if path == "/" or path == '':
    
        return root_page(environ, start_response)
    
    elif path_sections[1] == 'tracks':
        if len(path_sections) > 2 :
            if path_sections[2]=='' or path_sections[2]=='/':
    
                return exec('all_tracks_page(environ, start_response)')
            
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
    

def launch_app():
    with make_server('', 8000, route) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    launch_app()
