#!/usr/bin/env python3  
# EASY-INSTALL-ENTRY-SCRIPT: 'celery==3.1.23','console_scripts','celery'
from __future__ import absolute_import, unicode_literals
import os
import time
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracker.settings')

app = Celery('task')
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks('settings.INSTALLED_APPS')
# app.autodiscover_tasks()

# @app.task()
# def do_my_task():
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

