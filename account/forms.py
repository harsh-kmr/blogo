from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'year','branch', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ( 'first_name', 'last_name', 'username', 'bio', 'email', 'year','branch',)