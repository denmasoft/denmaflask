from werkzeug.wrappers import Request, Response


class CreateModelMiddleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        if request.path == '/create_model':
            res = Response(u'Verify first', mimetype='text/plain', status=401)
            return res(environ, start_response)
        return self.app(environ, start_response)
