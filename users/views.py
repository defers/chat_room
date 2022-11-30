from django.shortcuts import render

# Create your views here.
from django.views import generic

from users.models import UserProfile


class Profile(generic.UpdateView):
    model = UserProfile
    template_name = "chatroom/profile_edit.html"
    fields = ["name", "avatar"]
    success_url = "/chatroom"
