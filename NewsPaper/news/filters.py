from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'post': ['exact'],
            'category': ['exact'],
        }

#по названию
#по тегу
#позже указываемой даты