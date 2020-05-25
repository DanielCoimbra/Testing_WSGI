#! /usr/bin/python3

from wsgiref.simple_server import make_server


def handle_request(environ, start_response):
    ## TO-DO
    status = '200 OK'
    response_headers = [('Content-type','text/html')]
    path = environ['PATH_INFO']
    path_sections = path.split('/')

    if path == "/" or path == '':
        result = template("'root'")
        
    
    else:
        if path_sections[1] == 'hello':
            if len(path_sections) > 2:
                result = template('Hello ' + path_sections[2])
            else:
                result = template('Hello world')
        else:
            status = '404 NOT FOUND'
            result = template('not a valid', True)#Erro = True

    start_response(status, response_headers)
    return [result]



def template(path, error= False):
    if error:
        html = '''
        <!DOCTYPE HTML>

        <html>
            <h1>ERROR 404.</h1>
            <h4>        RESOURCE NOT FOUND.</h4>
        </html>
         '''
    else:
        html = '''
        <!DOCTYPE HTML>

        <html>
            <h1>This is  {}  directory.</h1>
        </html>'''.format(path)
        
    return html.encode('utf-8')


with make_server('', 8000, handle_request) as httpd:
    
    print('\nServing on port 8000...''\nTo finish the application process, press Ctrl+C\n\n')
   
    httpd.serve_forever()