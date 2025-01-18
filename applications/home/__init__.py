from __future__ import absolute_import, unicode_literals

# Importa explícitamente las tareas de esta app para asegurarte de que Celery las detecta
from .tasks import print_message, example_task
