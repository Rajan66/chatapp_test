from django.urls import path

from .views import chat_room, index

urlpatterns = [
    path("", index, name="chat-home"),
    path("<str:room_name>/", chat_room, name="chat-room"),
]
