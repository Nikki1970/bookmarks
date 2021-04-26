from django.urls import path
from . import views
app_name="bookmarksapp"
urlpatterns=[
    path('', views.BookMarkListView.as_view(), name="list"),
    path('new/', views.bookmark_new, name="new"),
    path('edit/<int:pk>/', views.bookmark_edit, name="edit"),
    path('delete/<int:pk>/', views.deleteBookMark, name="delete"),
    path('folders/', views.folder_list, name="folder-list"),
    path('folders/bookmark/<int:pk>', views.folder_bookmarks, name="folder-bookmarks")
]