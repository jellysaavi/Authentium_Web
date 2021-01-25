# from __future__ import absolute_import, unicode_literals

# import os

# from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authentium.settings.__init__")

# app = Celery('authentium')

# app.config_from_object('django.conf:settings', namespace='AUTHENTIUM_CELERY')

# app.conf.broker_url = 'redis://localhost:6379/0'

# app.autodiscover_tasks()