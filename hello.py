#! /usr/bin/python3

def app(environ,start_response):
    status = '200 OK'
    headers = [('Content-type','text/plain; charset=utf-8'),('Content_length', len('Hello World!'))]

    start_response(status, headers)

    return b'Hello World!'
