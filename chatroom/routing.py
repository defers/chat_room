from django.urls import re_path, path

from chatroom import consumers

websocket_urlpatterns = [
                    path(
                        'ws/chatroom/<int:id>', consumers.ChatRoomConsumer.as_asgi()
                    ),
                ]