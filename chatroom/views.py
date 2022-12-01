
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from chatroom import service
from chatroom.forms import CreateChatroomForm
from chatroom.models import ChatRoom


class AuthenticatedMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return super(AuthenticatedMixin, self).dispatch(request, *args, **kwargs)


class ChatList(AuthenticatedMixin, TemplateView):

    template_name = "chatroom/chat.html"

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chatrooms'] = service.find_chatrooms_not_deleted_ordered_by_created_date()
        return context


class ChatRoomView(AuthenticatedMixin, TemplateView):

    template_name = "chatroom/chat room.html"

    @transaction.atomic
    def get_context_data(self, **kwargs):
        chatroom = ChatRoom.objects.get(id=kwargs['id'])
        messages = chatroom.message_set.all()
        active_users = chatroom.users.filter(~Q(username=self.request.user.username))

        context = super().get_context_data(**kwargs)
        context['chatroom'] = chatroom
        context['messages'] = messages
        context['active_users'] = active_users

        return context

@transaction.atomic
def delete_chat_room(request, id):
    if not request.user.is_authenticated:
        return redirect('users:login')

    chatroom = service.find_chatroom_by_id(id)
    service.set_chat_room_delete(chatroom)
    return redirect("chatroom:chat")


class CreateChatRoomView(AuthenticatedMixin, View):
    @transaction.atomic
    def get(self, request):
        template = "chatroom/create_chatroom.html"
        form = CreateChatroomForm()
        context = {
            "form": form
        }
        return render(request, template, context)

    @transaction.atomic
    def post(self, request):
        chatroom_f = CreateChatroomForm(request.POST)
        if chatroom_f.is_valid():
            chatroom = chatroom_f.save(commit=False)
            chatroom.author = request.user.userprofile
            chatroom.save()

        return redirect("chatroom:chat")


