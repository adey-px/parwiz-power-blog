""" 
Optionally: 'from django.forms import ModelForm'
in place of 'from django import forms'
"""
from django import forms
from django.contrib.auth.models import User


# User Login form
class LoginForm(forms.Form):
    """
    User login with simple html form.
    Indicate fields for form in login page.
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# User Registration logic
class UserRegistration(forms.ModelForm):
    """
    User registration using django-crispy-forms
    using built in django User model
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

    def clean_password_2(self):
        checker = self.cleaned_data
        if checker["password1"] != checker["password2"]:
            raise forms.ValidationError("Oops! passwords failed to match")

        return checker["password2"]
