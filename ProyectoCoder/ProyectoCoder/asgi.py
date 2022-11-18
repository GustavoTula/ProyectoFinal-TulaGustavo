
import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import AppRoom.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoCoder.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            AppRoom.routing.websocket_urlpatterns
        )
    )
     

})
