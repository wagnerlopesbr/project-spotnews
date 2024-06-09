from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category, User
from news.forms import CategoryForm, NewsForm
from django.http import HttpResponseRedirect


def handle_form(request, function):
    if request.method == "POST":
        form = function(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = function()
    return form


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
    form = handle_form(request, CategoryForm)
    if isinstance(form, HttpResponseRedirect):
        return form
    context = {
        'form': form
    }
    return render(request, 'categories_form.html', context)


def news_form(request):
    form = handle_form(request, NewsForm)
    if isinstance(form, HttpResponseRedirect):
        return form
    categories = Category.objects.all()
    users = User.objects.all()
    context = {
        'form': form,
        'categories': categories,
        'users': users
    }
    return render(request, 'news_form.html', context)
