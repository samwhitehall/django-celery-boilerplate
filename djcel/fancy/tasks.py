import logging
import random
import string
import time

from celery import shared_task


class ExpensiveObject():
    def __init__(self):
        self.id_ = ''.join(
            random.choice(string.ascii_lowercase) for _ in range(6))

        logging.info('>> initialising ExpensiveObject ' + self.id_)
        time.sleep(5)
        logging.info('<< initialised ExpensiveObject ' + self.id_)

    def task(self, word):
        return '{} (from {})'.format(word.upper(), self.id_)

expensive_object = ExpensiveObject()


@shared_task
def expensive_task(word):
    logging.info('>> requesting `expensive_task` with ' + word)
    return expensive_object.task(word)
