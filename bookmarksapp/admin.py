from django.contrib import admin

# Register your models here.
from bookmarksapp.models import BookMark, Folder

admin.site.register(BookMark)
admin.site.register(Folder)
