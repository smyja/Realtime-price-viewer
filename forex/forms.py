from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    country = forms.CharField(max_length=100, help_text='Country of residence')
    title = forms.CharField(max_length=100, help_text='Mr/Mrs/Master/miss ')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phonenumber',
                  'email', 'password1', 'password2', 'country')
