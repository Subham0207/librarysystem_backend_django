"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from demo.consumers import *
from demo.token_auth import TokenAuthMiddleWare

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()

#ws://localhost:8000/test/
ws_patterns = [
    path('test/',async_demoConsumer)
]

application = ProtocolTypeRouter({
    'websocket' : TokenAuthMiddleWare
                    (
                        URLRouter(ws_patterns)    
                    ) 
})