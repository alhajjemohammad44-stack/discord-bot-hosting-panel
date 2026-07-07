"""Ultra minimal Vercel test"""
import json

def app(environ, start_response):
    """WSGI app - no Flask needed"""
    status = '200 OK'
    headers = [('Content-type', 'application/json')]
    body = json.dumps({
        'status': 'alive',
        'message': 'Hello from WSGI!'
    }).encode('utf-8')
    start_response(status, headers)
    return [body]
