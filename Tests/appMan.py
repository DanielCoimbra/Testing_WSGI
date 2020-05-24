#! /usr/bin/python3

from wsgiref.simple_server import make_server


def handle_request(environ, start_response):
    ## TO-DO
    status = '200 OK'
    response_headers[('Content-type','text/html')]
    result = b'Not Found'
    path = environ['PATH_INFO']
    if path == '' or path == '/':
        result=html.template("'root'")
    path_sections = path.split("/")

    if path_sections[1] == "hello":
        if len(path_sections) > 2:
            result = html.template("Hello " + path_sections[2])
        else:
            result = html.template("Hello world")
    else:
        result = html.template("not a valid")

    start_response(status, response_headers)

class AppsManager:
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        
    def __iter__(self):
        status = '302 FOUND'
        response_headers = [('Content-type', 'text/html'), ('Location','http://google.com')]
        self.start(status, response_headers)
        path = self.getPath()
               
        yield self.servePage(path)
        
    
    def getPath(self): return self.environ.get('PATH_INFO')
    

    def servePage(self, path):
        import html, re
        subdirlist = re.split('/', path)
        
        if not subdirlist[1]:
            return html.template('\'root\'', "")
    
        elif subdirlist[1] == 'hello':

            if len(subdirlist) > 2:
                if re.search('([0-9]|[a-zA-Z])*',subdirlist[2]):

                    return html.template('Hello '+ subdirlist[2])
                else:
                    return html.template('not a valid')
            else:
                return html.template('hello world')
        
        elif subdirlist[1] =='ola':

            return html.template('ola mundo')
        
        else:

            return html.template('not a valid')

with make_server('', 8000, AppsManager) as httpd:
    
    print('\n\nServing on port 8000...''\n\nTo finish the application process, press Ctrl+C\n\n')
   
    httpd.serve_forever()

'''
Begin reading Mapper and Routes.

'''