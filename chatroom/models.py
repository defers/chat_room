from channels.db import database_sync_to_async
from django.db import models
from chat_room.utils import get_class_representation
import users.models as user_models


class ChatRoom(models.Model):
    name = models.CharField(max_length=150, db_column="name", blank=False)
    description = models.CharField(max_length=250, db_column="description", null=True)
    author = models.ForeignKey(to=user_models.UserProfile, on_delete=models.CASCADE, db_column="author")
    created_date = models.DateTimeField(auto_now_add=True, db_column="created_date")
    deleted = models.BooleanField(db_column="deleted", default=False)
    users = models.ManyToManyField(to=user_models.UserDB)

    class Meta:
        db_table = "chat_room"

    def __str__(self) -> str:
        return get_class_representation(self)

    @database_sync_to_async
    def add_user(self, user):
        self.users.add(user)

    @database_sync_to_async
    def remove_user(self, user):
        self.users.remove(user)


class Message(models.Model):
    profile = models.ForeignKey(to=user_models.UserProfile, on_delete=models.SET_NULL, db_column="user", null=True)
    chat_room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE, db_column="chat_room")
    message_text = models.CharField(max_length=250, db_column="message_text")
    created_date = models.DateTimeField(auto_now=True, db_column="created_date")
    deleted = models.BooleanField(db_column="deleted")

    class Meta:
        db_table = "message"

    def __str__(self):
        return get_class_representation(self)


