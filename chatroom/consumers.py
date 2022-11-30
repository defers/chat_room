import django
django.setup()

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import chatroom.service_async as chatroom_service
import users.service as users_service
from chatroom.models import ChatRoom

@database_sync_to_async
def getChatRoom(id):
    return ChatRoom.objects.get(id=id)

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_box_id = self.scope["url_route"]["kwargs"]["id"]
        self.group_id = "chat_%s" % self.chat_box_id

        user_profile = await users_service.get_user_profile_from_user(self.scope["user"])
        chatroom = await getChatRoom(self.chat_box_id)
        await chatroom.add_user(self.scope["user"])

        await self.channel_layer.group_add(self.group_id, self.channel_name)
        await self.accept()
        await self.channel_layer.group_send(
            self.group_id,
            {
                "type": "chatbox_users",
                "user_profile": user_profile,
            },
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        username = text_data_json["username"]
        msg = await chatroom_service.save_message_by_data(text_data_json, self.chat_box_id)
        avatar_img = await chatroom_service.get_avatar_url_from(msg)

        await self.channel_layer.group_send(
            self.group_id,
            {
                "type": "chatbox_message",
                "message": msg.message_text,
                "avatar_img": avatar_img,
                "username": username,
                "created_date": msg.created_date.strftime("%b. %d, %Y, %H:%M %p"),
            },
        )

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_id, self.channel_name)
        self.chat_box_id = self.scope["url_route"]["kwargs"]["id"]
        chatroom = await getChatRoom(self.chat_box_id)
        await chatroom.remove_user(self.scope["user"])

    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]
        created_date = event["created_date"]
        avatar_img = event["avatar_img"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "created_date": created_date,
                    "avatar_img": avatar_img

                }
            )
        )

    async def chatbox_users(self, event):
        user_profile = event["user_profile"]
        avatar_img = user_profile.avatar.url if user_profile.avatar else ""
        await self.send(
            text_data=json.dumps(
                {
                    "username": user_profile.name,
                    "avatar_img": avatar_img,
                }
            )
        )
