import tornado.ioloop

from servicos.Hello import HelloHandler
import os

API_PORT = os.environ.get('API_PORT') or 8881

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(API_PORT)
    tornado.ioloop.IOLoop.current().start()