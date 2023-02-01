from django.urls import path
from .views import article_page, article_detail


urlpatterns = [
    path("", article_page, name="article_page"),
    path("article/<slug:slug>/", article_detail, name="article_detail"),
]
