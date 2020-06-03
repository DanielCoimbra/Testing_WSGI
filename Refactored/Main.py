from wsgiref.simple_server import make_server

from root import root

app = root

from wsgiref import make_server

with make_server('', 8000, app) as httpd:
    
    print('\nServing on port 8000...''\nTo finish the application process, press Ctrl+C\n\n')
   
    httpd.serve_forever()
