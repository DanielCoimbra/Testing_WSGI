#! /usr/bin/python3

def app(environ, start_response):
    
    environment_variables = [
        "{}: {}".format(k,v) for (k,v) in sorted(environ.items())
    ]
    environment_variables ='\n'.join(environment_variables)
    
    status = '200 OK'  # HTTP Status
    headers = [ ('Content-type', 'text/plain; charset=utf-8'), ('Content-Length', str(len(environ_dict)))]  # HTTP Headers
    
    start_response(status, headers) #works as if return(status,headers, $returnArgument)
    return [str(environment_variables).encode('utf-8')] # bytes object
