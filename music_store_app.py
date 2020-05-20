#! /usr/bin/python3

from wsgiref.simple_server import make_server
from html import template, all_tracks


def music_store_app(environ, start_response):
    
    status = '200 OK'
    response_headers = [('Content-type','text/html')]
    path = environ['PATH_INFO']
    path_sections = path.split('/')

    if path == "/" or path == '':
        result = template("the Music Store Index")
        
    
    elif path_sections[1] == 'tracks'.casefold():
        
        if len(path_sections) > 2:
            if path_sections[2] != '' and path_sections[2] != '/':
                result = track_page(path_sections[3])
            else: result = all_tracks()
        else:
            result = all_tracks()
    elif path_sections[1] == 'artists'.casefold():
        result = artists_page()


    else:
            status = '404 NOT FOUND'
            result = template('erro', True) #  Parametro:Erro = True

    start_response(status, response_headers)
    return [result]


with make_server('', 8000, music_store_app) as httpd:
    
    print('\nServing on port 8000...''\nTo finish the application process, press Ctrl+C\n\n')
   
    httpd.serve_forever()