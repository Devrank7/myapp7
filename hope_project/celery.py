# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hope_project.settings')

app = Celery('hope_project')

# Используем настройки Django для настройки Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи в файлах tasks.py
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'send-welcome-email-every-morning': {
        'task': 'main.tasks.sums',
        'schedule': crontab(hour='2', minute='30', day_of_week='1'),
        'args': (16, 5),  # Пример аргумента
    },
}
