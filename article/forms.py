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

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    conf_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

    def clean_conf_password(self):
        checker = self.cleaned_data
        if checker["password"] != checker["conf_password"]:
            raise forms.ValidationError("Oops! passwords do not to match")

        return checker["conf_password"]


"""
Forms in django involves just creating form fields,
and insert them within html form tags in templates

Crispy forms have some built in properties like 
.cleaned_data, .errors, .ValidationError, and
built in form validation, etc  
"""
