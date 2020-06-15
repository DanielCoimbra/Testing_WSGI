#! /usr/bin/python3
from appMan import AppsManager
from wsgiref.simple_server import make_server

with make_server('', 8000, AppsManager) as httpd:
    
    print('\n\nServing on port 8000...''\n\nTo finish the application process, press Ctrl+C\n\n')
   
    httpd.serve_forever()