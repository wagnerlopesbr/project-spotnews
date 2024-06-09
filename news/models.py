from django.db import models
from django.core.exceptions import ValidationError as VError


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    role = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class News(models.Model):
    def title_validation(value):
        if len(value.split()) < 2:
            raise VError("O título deve conter pelo menos 2 palavras.")

    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        validators=[title_validation]
    )
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=False)

    def __str__(self):
        return self.title
