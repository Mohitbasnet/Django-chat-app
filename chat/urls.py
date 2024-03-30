from django.urls import path

from .import views
app_name = 'çhat'

urlpatterns = [
    path('api/create-room/<str:uuid>', views.create_room, name = "create-room"),
]
