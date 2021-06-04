import json
from datetime import datetime

def app(environ, start_response):
    """Simplest possible application object"""
    data = { \
        'time':datetime.now().strftime('%X %x'),
        'url': environ['HTTP_HOST'] + environ['PATH_INFO']
    }

    status = '200 OK'
    response_headers = [ ('Content-type', 'application/json') ]
    start_response(status, response_headers)
    dump = json.dumps(data)
    enc = 'utf-8'
    return [ bytes(dump, encoding=enc) ]
