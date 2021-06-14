from django import forms
from django.contrib.auth.forms import UserCreationForm  


class userform(UserCreationForm):
    forms=UserCreationForm()
    
