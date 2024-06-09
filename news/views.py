from django.shortcuts import render, get_object_or_404
from news.models import News


def home(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'home.html', context)


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    context = {
        'news': news
    }
    return render(request, 'news_details.html', context)
