#! /usr/bin/python3

from wsgiref.simple_server import make_server

class AppsManager:
    
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        
    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        path = self.getPath()
               
        yield self.servePage(path)
        
    
    def getPath(self): return self.environ.get('PATH_INFO')
    

    def servePage(self, path):
        import html, re
        subdirlist = re.split('/', path)
        
        if not subdirlist[1]:
            return html.index('\'root\'')
    
        elif subdirlist[1] == 'hello':

            if len(subdirlist) > 2:
                if re.search('[0-4]',subdirlist[2]):

                    return html.index('world\'s sub')
                else:
                    return html.index('not a valid')
            else:
                return html.index('hello world')
        
        elif subdirlist[1] =='ola':

            return html.index('ola mundo')
        
        else:

            return html.index('not a valid')


'''
Begin reading Mapper and Routes.

'''