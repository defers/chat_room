from chatroom.models import ChatRoom


def find_chatroom_by_id(id):
    return ChatRoom.objects.get(id=id)


def set_chat_room_delete(chatroom):
    chatroom.deleted = not chatroom.deleted
    chatroom.save()


def find_chatrooms_not_deleted_ordered_by_created_date():
    return ChatRoom.objects.filter(deleted=False).order_by("-created_date")