FROM python:3.6

# EXPOSE 8888

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["celery", "-A", "tasks", "worker", "-Q", "hello-world", "--loglevel=DEBUG"]