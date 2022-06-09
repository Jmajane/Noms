from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class createUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']