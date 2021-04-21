from celery import Celery
import os

CELERY_NAME = os.environ.get('CELERY_NAME') or 'hello'
CELERY_URI = os.environ.get('CELERY_URI') or 'amqp://guest:guest@localhost:5672'

app = Celery('hello', broker=CELERY_URI)

@app.task(name=CELERY_NAME)
def hello(args):
	print('Task \'hello-wold\' chamado com os parâmetros', args)
	return 'hello world'