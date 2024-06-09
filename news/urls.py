from django.urls import path
from news.views import home, news_details, category_form


urlpatterns = [
    path('', home, name='home-page'),
    path('<int:id>/', news_details, name='news-details-page'),
    path('', category_form, name='categories-form'),
]
