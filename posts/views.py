from django.views.generic import ListView

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'post_list.html'
