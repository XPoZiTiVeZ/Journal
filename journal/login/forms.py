from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'last_name', 'first_name', 'father_name', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'last_name', 'first_name', 'father_name')