# Sharing objects using Celery

Perhaps you have some resource that you would like to share between Django
threads, e.g. a large file you would **rather not** load for each thread.

(assuming that one-time loading is the expensive bit, not accessing/processing)

## Setup
### Install Django & Celery
`pip install -r requirements`

### Install a message broker
* OSX: `brew install rabbitmq`
* Debian: `apt-get install rabbitmq`

## Run
```
rabbitmq-server
cd djcel
celery -A djcel worker --loglevel=info
python manage.py runserver
```

Visit: http://localhost:8000/aardvark

## What's happening?
