# applications/home/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import YourModel
from .tasks import example_task

@receiver(post_save, sender=YourModel)
def execute_task_after_save(sender, instance, **kwargs):
    example_task.delay(instance.some_field, 10)  # Envía datos relacionados con el modelo
