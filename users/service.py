from channels.db import database_sync_to_async

from users.models import UserProfile, UserDB


def find_user_profile_by_user(user) -> UserProfile:
    return UserProfile.objects.filter(user=user).first()

def create_user_profile_by_user(user):
    user_profile = UserProfile(name=user.username, user=user)
    user_profile.save()

@database_sync_to_async
def find_profile_by_username(username) -> UserProfile:
    if username == "":
        raise UserDB.DoesNotExist("Username is empty")

    return UserProfile.objects.filter(user__username=username)[0]

@database_sync_to_async
def get_user_profile_from_user(user):
    return user.userprofile

