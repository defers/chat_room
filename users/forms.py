from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import UserDB


class RegisterForm(UserCreationForm):

   class Meta:
       model = UserDB
       fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

