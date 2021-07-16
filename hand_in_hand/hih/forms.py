from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Client, Provider

class UserSignup(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ClientSignupForm(ModelForm):
  class Meta:
    model = Client
    fields = ['pronouns', 'age']
