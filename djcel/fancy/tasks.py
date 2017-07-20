import logging
import random
import string
import time

from celery import shared_task
from celery.signals import worker_init


_expensive_objects = {}

class ExpensiveObject():
    def __init__(self):
        self.id_ = ''.join(
            random.choice(string.ascii_lowercase) for _ in range(6))

        print '>> initialising ExpensiveObject ' + self.id_
        time.sleep(10)
        print '<< initialised ExpensiveObject ' + self.id_

    def task(self, word):
        return '{} (from {})'.format(word.upper(), self.id_)


def _load_expensive_object(**kwargs):
    if not _expensive_objects:
        _expensive_objects['loaded'] = ExpensiveObject()


worker_init.connect(_load_expensive_object)


@shared_task
def expensive_task(word):
    logging.info('>> requesting `expensive_task` with ' + word)

    if 'loaded' not in _expensive_objects:
        raise Exception('Expensive object not yet loaded')

    expensive_object = _expensive_objects['loaded']
    return expensive_object.task(word)
