from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile



class createUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'name', 'favorite_food', 'bio', 'workout_days']  
        labels = {
                "profile_pic": ("Picture     "),
                "name": ("name  "),
                "favorite_food": ("Favorite Food   "),
                "bio": ("Bio   "),
                "workout_days": ("Workout Days    "),
                }
                