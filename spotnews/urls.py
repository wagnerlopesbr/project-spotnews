from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home-page"),
    path("<int:id>/", views.news_details, name="news-details-page"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
