# make sure the celery app is imported when django starts
from djcel.celery import app as celery_app
