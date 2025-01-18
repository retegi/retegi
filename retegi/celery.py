# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece la configuración predeterminada de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'retegi.settings')

app = Celery('retegi')

# Lee la configuración de Celery desde el archivo settings.py
# Todas las variables que comiencen con 'CELERY_' serán consideradas.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-detecta tareas en los módulos `tasks.py` de las aplicaciones instaladas.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

