
from django.urls import path, re_path
import chatroom.views as views


app_name = "chatroom"

urlpatterns = [
    re_path(r'^$', views.ChatList.as_view(), name="chat"),
    re_path(r'^(?P<id>\d+)/$', views.ChatRoomView.as_view(), name="chatroom"),
    re_path(r'^(?P<id>\d+)/delete$', views.delete_chat_room, name="chatroom_delete"),
    re_path(r'^add$', views.CreateChatRoomView.as_view(), name="chatroom_add")
]