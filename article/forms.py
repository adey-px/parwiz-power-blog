""" 
Optionally: Use ModelForm from django.forms
"""
from django import forms


#
class LoginForm(forms.Form):
    """create fields for login form"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
