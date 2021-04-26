from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookmarksapp.models import BookMark
from django.views import generic
from .forms import BookMarkForm
from .filters import BookmarkFilter

class BookMarkListView(generic.ListView):
    model = BookMark

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookmarkFilter(self.request.GET, queryset=self.get_queryset())
        return context

def bookmark_new(request):
    form = BookMarkForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bookmarksapp:list')
    context={
        'form': form
    }
    return render(request, 'bookmarksapp/bookmark_new.html', context)

def bookmark_edit(request, pk):
    bookmark = BookMark.objects.get(id = pk)
    form = BookMarkForm(request.POST or None, instance = bookmark)
    if form.is_valid():
        form.save()
        return redirect('bookmarksapp:list')
    context = {
        'form' : form
    }
    return render(request, 'bookmarksapp/bookmark_new.html', context)

def deleteBookMark(request, pk):
    bookmark = BookMark.objects.get(id=pk)
    bookmark.delete()
    # if request.method =="POST":
    #     bookmark.delete()
    #     return redirect('list-of-events')
    # context = {'bookmark': bookmark}
    return redirect('bookmarksapp:list')

