from celery import Celery
import os

CELERY_NAME = os.environ.get('CELERY_NAME') or 'hello'
CELERY_URI = os.environ.get('CELERY_URI') or 'amqp://guest:guest@localhost:5672'

app = Celery(CELERY_NAME, broker=CELERY_URI)

@app.task(name='hello-world')
def hello(args):
	print('Task chamada com os parâmetros', args)
	return 'hello world'