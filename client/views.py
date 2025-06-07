from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from writer.models import Article
from .models import Subscription


@login_required(login_url='login')
def client_dashboard(request):
    return render(request, 'client/client-dashboard.html')



@login_required(login_url='login')
def browse_articles(request):

    try:
        subDetails = Subscription.objects.get(user = request.user, is_activate=True)

    except:
        return redirect('client_dashboard')
    
    current_subscription_plan = subDetails.subscription_plan
    
    if current_subscription_plan == 'Standard':
        articles = Article.objects.all().filter(is_premium=False).order_by('-date_posted')
    elif current_subscription_plan == 'Premium':
        articles = Article.objects.all().order_by('-date_posted')
    else:
        articles = Article.objects.none()

    context = {'AllClientArticles': articles}

    return render(request, 'client/browse-articles.html', context=context)

