from django.shortcuts import render
from django.http import HttpResponse
from bookmarksapp.models import BookMark
from django.views import generic

class BookMarkListView(generic.ListView):
    model = BookMark