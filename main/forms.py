from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Talk,User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)

class LoginForm(AuthenticationForm):
    pass

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "新しいユーザー名"}
        help_texts = {"username": ""}

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
        labels = {"email":"新しいE-mailアドレス"}