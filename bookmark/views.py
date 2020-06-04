from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from bookmark.models import Bookmark

class BookmarkList(ListView):
    model = Bookmark
    paginate_by = 3

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']       # <form>
    template_name_suffix = '_update'    # bookmark_update.html
    success_url = reverse_lazy('bookmark:list')