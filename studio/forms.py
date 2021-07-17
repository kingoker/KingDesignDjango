from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from .models import PhoneNumber


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProneNumberForm(ModelForm):

    class Meta:
        model = PhoneNumber
        fields = ['number']


