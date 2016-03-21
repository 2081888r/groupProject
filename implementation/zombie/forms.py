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
    class Meta:
        model = UserProfile
        fields = ('avatar',)
        
class ImageUploadForm(forms.Form):
    new_profile_pic = forms.ImageField()