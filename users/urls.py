
from django.urls import path, re_path
import users.views as views


app_name = "users"

urlpatterns = [
    re_path(r'^profile/(?P<pk>\d+)$', views.Profile.as_view(), name="profile")
]