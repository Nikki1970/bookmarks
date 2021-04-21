from django.urls import path
from . import views
app_name="bookmarksapp"
urlpatterns=[
    path('', views.index, name="index")
]