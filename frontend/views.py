from django.views.generic import ListView, TemplateView, DetailView
from .models import Post


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogPageView(ListView):
    model = Post
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'