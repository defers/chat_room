from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserDB(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class UserProfile(models.Model):
    name = models.CharField(max_length=150, db_column="name", blank=False, null=False)
    user = models.OneToOneField(to=UserDB, on_delete=models.CASCADE, db_column="user")

    class Meta:
        db_table = "user_profile"