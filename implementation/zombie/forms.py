from django import forms
from django.contrib.auth.models import User
from zombie.models import UserProfile
from django.db.models.fields.files import ImageField
from django.db import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required = False)
    full_name = forms.CharField(required = False)
    class Meta:
        model = UserProfile
        fields = ('full_name', 'avatar')
        
