from django.urls import path
from .views import *


urlpatterns = [
    path("", article_page, name="article_page"),
    path("article/<slug:slug>/", article_detail, name="article_detail"),
    path('login/', user_login, name='login')
]
