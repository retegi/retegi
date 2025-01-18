from celery import shared_task

@shared_task
def example_task(x, y):
    print("hola desde la tarea programada")
    return x + y

@shared_task
def print_message():
    print("prueba123")
    return "Mensaje impreso: prueba123"
