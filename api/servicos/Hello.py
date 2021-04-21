import tornado.web
from celery import Celery
import os

CELERY_URI = os.environ.get('CELERY_URI') or 'amqp://guest:guest@localhost:5672'

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        celery = Celery(
            'api',
            broker=CELERY_URI,
            backend=CELERY_URI.replace('pyamqp://', 'rpc://').replace('amqp://', 'rpc://'),
        )
        celery.send_task('hello-world', args=[{'teste':123, 'outro_teste':321}], kwargs={}, queue='hello-world')
        self.write("Sua tarefa será executada em background")