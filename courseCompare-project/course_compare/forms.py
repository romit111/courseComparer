from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=30)
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.IntegerField()
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'country', 'city', 'state', 'pincode', 'birth_date','password1','password2')
