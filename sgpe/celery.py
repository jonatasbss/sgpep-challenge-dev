import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgpe.settings')

app = Celery('sgpe')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# @app.tasks(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

