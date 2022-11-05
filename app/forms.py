from django import forms
from app.models import *

class Username(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']