"""
Two ways to create forms '.Form' or '.ModelForm'
Note .Form requires stating all the fields manually
while .ModelForm uses built in django User model to 
select required fields as string.

Load forms as 'form.as_p' or 'form|crispy' in templates 
where they are used. Rem to install django-crispy-forms.
"""
from django import forms
from django.contrib.auth.models import User
from .models import Article


# Article Creation form
class CreateArticleForm(forms.ModelForm):
    """
    Form to create or upload article.
    Only title & desc are required. Other
    fields in Article model are auto created.
    """

    class Meta:
        model = Article
        fields = ("title", "description")


# Article Update form
class UpdateArticleForm(forms.ModelForm):
    """
    Form to update article.
    """

    class Meta:
        model = Article
        fields = ("title", "description")


# User Registration form
class RegisterForm(forms.ModelForm):
    """
    Create form object for registration.
    Default registration fields can be seen in
    django Admin|User|Add User from built in
    django User model. Select fields you want
    in parenthesis as string, under Meta class.
    """

    # create & confirm password fields manually
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    conf_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    # select other fields using User model
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

    # clean data, check password fields
    def clean_conf_password(self):
        cd = self.cleaned_data
        if cd["password"] != cd["conf_password"]:
            raise forms.ValidationError("Passwords do not to match")

        return cd["conf_password"]


# User Login form
class LoginForm(forms.Form):
    """
    Create form object for login.
    The form data is cleaned in views.py
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
