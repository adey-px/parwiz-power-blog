from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", article_page, name="article_page"),
    path("article/<slug:slug>/", article_detail, name="article_detail"),
    path("register/", register, name="register"),
    path('login/', user_login, name='user_login'),
    # path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

"""
In line 10, django built in LoginView is used
as alternative to custom login url in line 9.
To use it, create folder named registration in 
templates, with login.html inside. They both 
use same view name='user_login' in views.py. 
Also set some required vars in settings.py.

For logout, create logged_out.html in same
registration folder, and its route in urls.py
"""