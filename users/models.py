
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from chat_room.utils import get_class_representation


class UserDB(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username + "(" + self.first_name + " " + self.last_name + ")"


class UserProfile(models.Model):
    name = models.CharField(max_length=150, db_column="name", blank=False, null=False)
    user = models.OneToOneField(to=UserDB, on_delete=models.CASCADE, db_column="user", unique=True)
    avatar = models.ImageField(upload_to="users", db_column="avatar", null=True)

    class Meta:
        db_table = "user_profile"

    def __str__(self) -> str:
        return str(self.user)