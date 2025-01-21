import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from applications.assistant.urls import websocket_urlpatterns



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'retegi.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Manejo de solicitudes HTTP
    "websocket": AuthMiddlewareStack(  # Manejo de solicitudes WebSocket
        URLRouter(websocket_urlpatterns)  # Incluye las rutas WebSocket
    ),
})
