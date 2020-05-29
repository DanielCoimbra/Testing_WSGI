#! env python3

from wsgiref.simple_server import make_server
from html import *
from cgi import parse_qs, escape

def music_store_app(environ, start_response):
    
    status = '200 OK'
    response_headers = [('Content-type','text/html')]
    path = environ['PATH_INFO']
    path_sections = path.split('/')
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    if path == "/" or path == '':  #root directory
        result = template("", """<a href="http://127.0.0.1:8000/tracks"><p style="font-size:38px">Tracks</p></a><a href="http://127.0.0.1:8000/artists"><p style="font-size:38px">Artists</p></a>""")
        
    
    elif path_sections[1] == 'tracks'.casefold(): #tracks directory
        
        if len(path_sections) > 2:
            if path_sections[2] != '':
                if environ['REQUEST_METHOD'].casefold() == 'get':
                    result = template("Track Page", track_page(path_sections[2]))

                elif environ['REQUEST_METHOD'].casefold() == 'post':
                    try:
                        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
                    except (ValueError):
                        request_body_size = 0
                    request_body = environ['wsgi.input'].read(request_body_size)
                    d = parse_qs(request_body)
                    track= d[b'Track']
                    composer= d[b'Composer']
                    track = str(track)
                    track = escape(track)
                    composer = str(composer)
                    composer = escape(composer)
                    track_form_handler(path_sections[2], track[3:len(track)-2], composer[3:len(composer)-2])
                    start_response('302 FOUND', response_headers)
                    result =  template("Track Page", track_page(path_sections[2]))
                    return [result]
                    
                    
            else: 
                result = template("Tracks",all_tracks())
        
        else:
            result = template("Tracks",all_tracks())
    
    elif path_sections[1] == 'artists'.casefold(): # artists directory
        result = template("Artists Discography",artists_page())

    else:
        status = '404 NOT FOUND'
        result = template('404 NOT FOUND', """<pre style="font-size:18px;">                                RESOURCE NOT FOUND.</pre>""")

    start_response(status, response_headers)
    return [result]


with make_server('', 8000, music_store_app) as httpd:
    
    print('\nServing on port 8000...''\nTo finish the application process, press Ctrl+C\n\n')
   
    httpd.serve_forever()