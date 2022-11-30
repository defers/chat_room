"""
ASGI config for chat_room project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

import chatroom.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_room.settings')

# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": get_asgi_application(),
#     "websocket": AllowedHostsOriginValidator
# })

# Handles routing protocols for Django Channels
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                chatroom.routing.websocket_urlpatterns
            )
        )
        # # Points root routing to chat/routing.py
        # "websocket": AllowedHostsOriginValidator(
        #    AuthMiddlewareStack(
        #       URLRouter(chatroom.routing.websocket_urlpatterns)
        #    )
        # ),
    }
)