
from django.urls import path, re_path
import users.views as views
from django.contrib.auth import views as auth_views


app_name = "users"

urlpatterns = [
    re_path(r'^profile/(?P<pk>\d+)$', views.Profile.as_view(), name="profile"),
    re_path(r'^register$', views.Register.as_view(), name="register"),
    re_path(r'^login$', views.Login.as_view(), name="login"),
    re_path(r'^logout$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]