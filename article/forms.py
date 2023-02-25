"""
Two ways to create forms are .Form | .ModelForm
.Form requires stating all the fields manually
while .ModelForm uses built in django User model
and to select the fields as string.
"""
from django import forms
from django.contrib.auth.models import User


# Registration form
class RegisterForm(forms.ModelForm):
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
        cd = self.cleaned_data
        if cd["password"] != cd["conf_password"]:
            raise forms.ValidationError("Oops! passwords do not to match")

        return cd["conf_password"]


# Login form
class LoginForm(forms.Form):
    """
    User login with simple html form.
    Indicate fields for form in login page.
    """

    # create fields manually
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


"""
Forms in django involves just creating form fields,
and insert them within html form tags in templates

Crispy forms have some built in properties like 
.cleaned_data, .errors, .ValidationError, and
built in form validation, etc. They also come
with styling by dafault.
"""
