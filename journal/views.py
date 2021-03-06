from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Article
from .forms import ArticleForm

import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def account(request):
    user_articles = request.user.article_set.all().order_by('-created_at')[:5]
    return render(request, 'journal.html', locals())

@login_required
def new_article(request):
    if request.method == 'POST':
        article_data = request.POST.copy()
        article_data['author_id'] = request.user.id
        article_data['published_at'] = datetime.datetime.now()
        article_data['is_published'] = True

        form = ArticleForm(article_data)
        if form.is_valid():
            form.save()
            return redirect('/journal/')
    else:
        article = Article(author=request.user)
        form = ArticleForm(instance=article)

    return render(request, 'article/new.html', locals())

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        article_data = request.POST.copy()
        article_data['author_id'] = request.user.id
        article_data['published_at'] = datetime.datetime.now()
        article_data['is_published'] = True
        if form.is_valid():
            form.save()
            return redirect('/journal/')
    return render(request, 'article/edit.html', locals())



def view_article(request, username, slug):
    user = get_object_or_404(User, username=username)
    article = get_object_or_404(user.article_set, slug=slug)
    return render(request, 'article/show.html', locals())
