# Sharing objects using Celery

Perhaps you have some resource that you would like to share between Django
threads, e.g. a large file you would **rather not** load for each thread.

(assuming that one-time loading is the expensive bit, not 
accessing/processing). Maybe you will find this boilerplate useful too.

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
We have an expensive object that does something fancy 
(`fancy/tasks.py:ExpensiveObject`). Maybe it is loading something big into
memory. It is definitely not just sleeping.

Instead of instantiating this class in the view function (i.e. on every
HTTP request), it is instantiated in the module scope of `fancy/tasks.py`, i.e.
when starting the Celery worker server.

The task (`fancy/tasks.py:ExpensiveObject.expensive_task`)  then be 
called asynchronously in the view (`fancy/views.py:expensive_view`. 

Test this at `localhost:8000/aardvark`.

NB. add a timeout to `.get()` in production code. See `djcel/celery.py` for
task discovery logic.
