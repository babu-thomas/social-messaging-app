from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return models.Post.objects.order_by('-date')


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = models.Post
    fields = ['message']
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostCreateView(CreateView):
    model = models.Post
    template_name = 'post_new.html'
    fields = ['message']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
