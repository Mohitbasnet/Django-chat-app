from django.urls import path

from . import consumers 


websocket_urlpatters = [
    path('sw/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]