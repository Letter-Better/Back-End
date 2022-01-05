import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from campaign import routers as campaign_routers
from online import routers as online_routers
from online.authentications import JWTAuthenticationMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JWTAuthenticationMiddleware(
        URLRouter(
            online_routers.websocket_urlpatterns
        ),
    ),
})

