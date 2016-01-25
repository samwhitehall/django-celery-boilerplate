"""
Minimal django settings.
"""

# Django settings
SECRET_KEY = 'topsecretkey'
ALLOWED_HOSTS = ['localhost']
ROOT_URLCONF = 'djcel.urls'

INSTALLED_APPS = [
    'fancy',
]

# Celery settings
BROKER_URL = 'amqp://guest@localhost//'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'rpc://'
CELERY_RESULT_PERSISTENT = False
