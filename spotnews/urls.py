from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"news", views.NewsViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("", views.home, name="home-page"),
    path("news/<int:id>/", views.news_details, name="news-details-page"),
    path("categories/", views.category_form, name="categories-form"),
    path("news/", views.news_form, name="news-form"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
