from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from .forms import LoginForm, UserRegistration
from django.contrib.auth import authenticate, login


# All articles page
def article_page(request):
    """
    Get all articles in db to display on page
    """
    articles = Article.objects.all().order_by("published")
    return render(request, "article/articles.html", {"articles": articles})


# Each article detail
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
        register_form = UserRegistration(request.POST)

        if register_form.is_valid():
            new_account = register_form.save(commit=False)
            new_account.set_password(register_form.cleaned_data["conf_password"])
            new_account.save()

            return render(
                request, "register-done.html", {"register_form": register_form}
            )
    else:
        register_form = UserRegistration()
    return render(request, "register.html", {"register_form": register_form})


# User Login
def user_login(request):
    """
    User login with html form defined in forms.py
    The form has two fields - username and password.
    Alternatively, use django built in LoginView
    as stated in urls.py
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            checker = form.cleaned_data
            user = authenticate(
                request, username=checker["username"], password=checker["password"]
            )
            if user is not None:
                login(request, user)
                return HttpResponse("Success, you are logged in")
        else:
            return HttpResponse("Oops! incorrect username and/or password")
    else:
        form = LoginForm()
    return render(request, "login-page.html", {"form": form})
