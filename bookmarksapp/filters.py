import django_filters
from .models import BookMark, Folder

class BookmarkFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BookMark
        fields = ['name', 'folder']