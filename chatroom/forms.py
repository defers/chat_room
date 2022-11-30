from django import forms

from chatroom.models import ChatRoom


class CreateChatroomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = [
            "name",
            "description"
        ]
