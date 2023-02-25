""" 
Ensure to pass exact string used as path name here 
to the href link as url to open the template.
Refer to articles.html href that opens article_detail
"""
from django.urls import path
from .views import *
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

urlpatterns = [
    path("", articles_page, name="article_page"),
    path("article/<slug:slug>/", article_detail, name="article_detail"),
    path("register/", register, name="register"),
    # path("login/", user_login, name="user_login"),
    # 
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-change/", PasswordChangeView.as_view(), name="password-change"),
    path(
        "password-change/done",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]

"""
In line 15, django built in LoginView is used
as alternative to custom login view in line 14.
To use it, create folder named registration in 
templates, with login.html inside.

The LoginView looks for any login form inside
registration/login.html as its template. Neeed
to set some required vars in settings.py.

NB: update name='login' as seen in line 15,
use same in template href where user clicks

For logout, create logged_out.html in same
registration folder, and its route in urls.py
"""
