""" docstring here """
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.

# All articles page
def article_page(request):
    """get all articles in db to display on page"""

    articles = Article.objects.all().order_by("published")
    return render(request, "articles.html", {"articles": articles})


# Each article details
def article_detail(request, slug):
    """get and disply detail of each article in db.
    'article' here is passed in article-detail href link.
    slug for aricle instance is created in signals.
    """

    article = get_object_or_404(Article, slug=slug)
    return render(request, "article-detail.html", {"article": article})
