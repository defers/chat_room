from users.models import UserProfile


def find_user_profile_by_user(user) -> UserProfile:
    return UserProfile.objects.filter(user=user).first()

def create_user_profile_by_user(user):
    user_profile = UserProfile(name=user.username, user=user)
    user_profile.save()

