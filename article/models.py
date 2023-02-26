""" 
Artilce model is written with custom fields.
Note that django built in User model is used 
for user registration
"""
from django.db import models
from django.contrib.auth.models import User


# Custom Article model
class Article(models.Model):
    """
    Article model with slug included for use
    in signals, views, urls and article-detail page.
    Slug is passed as title in article-detail page.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # show each article by title in admin
    def __str__(self):
        return self.title
