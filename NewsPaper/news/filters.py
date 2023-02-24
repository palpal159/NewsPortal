from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post


class PostFilter(FilterSet):
    post_date = DateFilter('post_date__date', label='Найти посты по заданной дате')

    class Meta:
        model = Post
        fields = {
            'post': ['exact'],
            'author': ['exact'],
            'category': ['exact'],
        }
        widget = forms.DateInput()

#по названию
#по тегу
#по дате