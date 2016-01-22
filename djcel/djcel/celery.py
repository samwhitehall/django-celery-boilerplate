from __future__ import absolute_import

import os

from celery import Celery

# import django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcel.settings')
from django.conf import settings

# celery app
app = Celery('djcel')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print 'Request: {0!r}'.format(self.request)
