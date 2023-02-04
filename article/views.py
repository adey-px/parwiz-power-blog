""" docstring here """
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from .forms import LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.

# All articles page
def article_page(request):
    """get all articles in db to display on page"""

    articles = Article.objects.all().order_by("published")
    return render(request, "article/articles.html", {"articles": articles})


# Each article details
def article_detail(request, slug):
    """get and disply detail of each article in db.
    'article' here is passed in article-detail href link.
    slug for aricle instance is created in signals.
    """

    article = get_object_or_404(Article, slug=slug)
    return render(request, "article/article-detail.html", {"article": article})


# Login page logic
def user_login(request):
    """user login page logic"""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )

            if user is not None:
                login(request, user)
                return HttpResponse("Success, you are logged in")

        else:
            return HttpResponse('Oops, failed to be logged in')
    
    else:
        form = LoginForm()

    return render(request, 'login-page.html', {'form': form})