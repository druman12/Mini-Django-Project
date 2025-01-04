from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:   # M always capital othervise no modelform found error occure...
        model=Tweet
        fields=['text','photo']  #name of the model fields which we initialized in models.py
        
class UserRegistrationForm(UserCreationForm):
    #add new one field on this gien form
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')