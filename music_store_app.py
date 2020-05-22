#! /usr/bin/python3

from wsgiref.simple_server import make_server
from html import template, all_tracks, track_page, artists_page


def music_store_app(environ, start_response):
    
    status = '200 OK'
    response_headers = [('Content-type','text/html')]
    path = environ['PATH_INFO']
    path_sections = path.split('/')

    if path == "/" or path == '':  #root directory
        result = template("", "")
        
    
    elif path_sections[1] == 'tracks'.casefold(): #tracks directory
        
        if len(path_sections) > 2:
            if path_sections[2] != '' and path_sections[2] != '/':
                result = template("Track Page", track_page(path_sections[2]))
            else: result = template("Tracks",all_tracks())
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