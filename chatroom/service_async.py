import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_room.settings')
import django
django.setup()

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from chatroom.models import ChatRoom, Message
from users import service as users_service
from chatroom import service


@database_sync_to_async
def find_chatroom_by_id(id):
    # return ChatRoom.objects.get(id=id)
    return service.find_chatroom_by_id(id)


async def save_message_by_data(data, chatroom_id) -> Message:
    message_text = data["message"]
    username = data["username"]

    # with transaction.atomic():
    profile = await users_service.find_profile_by_username(username)
    chatroom = await find_chatroom_by_id(chatroom_id)
    message = await save_message(message_text, profile, chatroom)
    return message


@database_sync_to_async
def save_message(message_text, profile, chatroom):
    message = Message(profile=profile, message_text=message_text, chat_room=chatroom, deleted=False)
    message.save()
    return message


@database_sync_to_async
def get_avatar_url_from(msg):
    return msg.profile.avatar.url