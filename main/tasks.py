import time

from celery import shared_task


@shared_task(time_limit=3600)
def sums(a, b):
    time.sleep(5)
    return a + b
