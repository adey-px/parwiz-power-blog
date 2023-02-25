from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


# Articles page
def articles_page(request):
    """
    Get all articles in db to display on page
    """
    articles = Article.objects.all().order_by("published")
    return render(request, "article/articles.html", {"articles": articles})


# Article detail
def article_detail(request, slug):
    """
    Get and display detail of each article in db.
    'article' here is passed in article-detail href link.
    slug for aricle instance is created in signals.
    """
    article = get_object_or_404(Article, slug=slug)
    return render(request, "article/article-detail.html", {"article": article})


# User Registration
def register(request):
    """
    Register user with crispy form defined in
    forms page as UserRegistration. Note commit
    is false not to save user until set_password.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["conf_password"])
            new_user.save()

            return render(request, "auth/register-done.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, "auth/register-form.html", {"form": form})


# Login & Authentication
def user_login(request):
    """
    User login with html form defined in forms.py
    The form has two fields - username and password.
    Alternatively, use django built in LoginView
    as stated in urls.py
    """
    if request.method == "POST":
        form = LoginForm(request.POST)

        # if form is valid, clean data from its fields
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            # allow login, if details are valid
            if user is not None:
                login(request, user)
                return HttpResponse("Success, you are logged in")
        else:
            return HttpResponse("Incorrect username and/or password")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})
