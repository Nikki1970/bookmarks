from django.urls import path
from . import views
app_name="bookmarksapp"
urlpatterns=[
    path('', views.BookMarkListView.as_view(), name="list")
]