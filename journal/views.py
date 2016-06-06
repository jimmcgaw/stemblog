from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm

import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def account(request):
    user_articles = Article.objects.filter(author=request.user)
    return render(request, 'account.html', locals())

def new_article(request):
    if request.method == 'POST':
        article_data = request.POST.copy()
        article_data['author_id'] = request.user.id
        article_data['published_at'] = datetime.datetime.now()
        article_data['is_published'] = True

        form = ArticleForm(article_data)
        if form.is_valid():
            form.save()

    else:
        article = Article(author=request.user)
        form = ArticleForm(instance=article)

    return render(request, 'new_article.html', locals())

def view_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'view_article.html', locals())
