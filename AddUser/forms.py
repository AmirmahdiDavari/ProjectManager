from django import forms
from django.forms.fields import EmailField

class emailLoginValidation(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)