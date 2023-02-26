"""
Forms imported from forms.py may be optionally
loaded with crispy tags in templates. Crispy
forms have additional benefits when used.

Custom Login view won't be used if django built-in
LoginView is used. Refer urls.py for more details.
"""
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import CreateArticleForm, LoginForm, RegisterForm, UpdateArticleForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Create article
@login_required
def create_article(request):
    """
    View to create new article
    """
    form = CreateArticleForm(request.POST)

    # link auth user to article, save
    if request.method == "POST":
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            # redirect to home page
            return redirect("articles-list")

    else:
        form = CreateArticleForm(request.POST)
    return render(request, "article/article-new.html", {"form": form})


# Articles list
def articles_list(request):
    """
    Get all articles from db,
    last in first out, in pages.
    """
    articles = Article.objects.all()[::-1]
    paginator = Paginator(articles, 3)
    page = request.GET.get("page")

    try:
        pagination = paginator.page(page)

    except PageNotAnInteger:
        pagination = paginator.page(1)

    except EmptyPage:
        pagination = paginator.page(paginator.num_pages)

    return render(
        request, "article/articles-list.html", {"articles": pagination, "page": page}
    )



# Article detail
def article_detail(request, slug):
    """
    Get and display detail of each article in db.
    'article' here is passed in article-detail href link.
    slug for aricle instance is created in signals.
    """
    article = get_object_or_404(Article, slug=slug)
    return render(request, "article/article-detail.html", {"article": article})


# Update article
@login_required
def update_article(request, slug):
    """
    View to update article
    """
    article = get_object_or_404(Article, slug=slug)
    form = UpdateArticleForm(request.POST or None, instance=article)

    if form.is_valid():
        article.save()
        return redirect("articles-list")

    return render(request, "article/article-update.html", {"form": form})


# Delete article
@login_required
def delete_article(request, slug):
    """
    View to delete article
    """
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect("articles-list")


# Custom Registration
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

            return render(request, "custom/register-done.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, "custom/register-form.html", {"form": form})


# Custom Login
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
    return render(request, "custom/login.html", {"form": form})
