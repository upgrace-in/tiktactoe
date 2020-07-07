from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from tiktactoe_app.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r'new_game/(?P<game_id>[\w.@+-]+)/$', ChatConsumer)
                ]
            )
        )
    )
})