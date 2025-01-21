from django.urls import path
from . import consumers
from . import views

websocket_urlpatterns = [
    path('ws/assistant/', consumers.AssistantConsumer.as_asgi()),
]
urlpatterns = [
    path('assistant/', views.assistant_response, name='assistant_response'),
]