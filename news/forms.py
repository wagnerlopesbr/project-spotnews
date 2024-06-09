from django import forms
from news.models import Category, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'maxlength': 200,
                'required': True,
            }),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'maxlength': 200,
                'required': True,
            }),
            'content': forms.Textarea(),
            'author': forms.Select(attrs={
                'required': True,
            }),
            'created_at': forms.DateInput(attrs={
                'type': 'date',
                'required': True,
            }),
            'image': forms.FileInput(),
            'categories': forms.CheckboxSelectMultiple(),
        }
