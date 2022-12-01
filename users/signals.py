
# method for updating
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import UserDB
from users.service import find_user_profile_by_user, create_user_profile_by_user


@receiver(post_save, sender=UserDB, dispatch_uid="saved_user")
def create_user_profile(sender, instance, **kwargs):
    user_profile = find_user_profile_by_user(user=instance)
    if user_profile is None:
        create_user_profile_by_user(user=instance)





