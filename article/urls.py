""" 
Ensure to pass exact string used as path name here 
to the href link as url to open the template.
Refer to href link in articles-list.html 
"""
from django.urls import include, path
from .views import *
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

urlpatterns = [
    path("", articles_list, name="articles-list"),
    path("article/<slug:slug>/", article_detail, name="article-detail"),
    path("create-article/", create_article, name="create-article"),
    path("update-article/<slug:slug>/", update_article, name="update-article"),
    path("delete-article/<slug:slug>/", delete_article, name="delete-article"),
    path("register/", register, name="register"),
    # path("login/", user_login, name="user_login"),
    #
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-change/", PasswordChangeView.as_view(), name="password-change"),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    #
    # path('social-auth', include('social_django,urls', namespace='social'))
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
