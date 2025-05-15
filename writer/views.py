from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import HttpResponse
from .models import Article


@login_required(login_url='login')
def writer_dashboard(request):
    return render(request, 'writer/writer-dashboard.html')


@login_required(login_url='login')
def create_article(request):

    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            return redirect('my_articles')
        
    context = {'form': form}
    return render(request, 'writer/create-article.html', context=context)


@login_required(login_url='login')
def my_articles(request):
    current_user = request.user
    articles = Article.objects.filter(user=current_user)

    context = {'articles': articles}
    return render(request, 'writer/my-articles.html', context=context)
