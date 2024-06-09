from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from news.forms import CategoryForm


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


def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'categories_form.html', context)
