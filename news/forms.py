from django import forms
from news.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'maxlength': 200,
                'required': True,
            }),
        }
