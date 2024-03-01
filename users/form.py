from django.forms import ModelForm

from servicii import forms
from users.models import UserModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"