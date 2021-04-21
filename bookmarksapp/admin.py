from django.contrib import admin

# Register your models here.
from bookmarksapp.models import BookMark

admin.site.register(BookMark)