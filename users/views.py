from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from django.views.generic.base import View

from users.forms import RegisterForm
from users.models import UserProfile


class Profile(generic.UpdateView):
    model = UserProfile
    template_name = "chatroom/profile_edit.html"
    fields = ["name", "avatar"]
    success_url = "/chatroom"


class Register(View):

    def __init__(self):
        super().__init__()
        self.template = "users/register.html"

    def get(self, request):

        form = RegisterForm()
        context = {
            "form": form
        }

        return render(request, self.template, context)

    def post(self, request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except ValueError as e:
                print(e)

        else:
            print(form.errors)

        context = {
            "form": form
        }

        return render(request, self.template, context)
