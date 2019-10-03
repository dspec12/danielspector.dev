from django.urls import path
from .views import HomePageView, AboutPageView, BlogPageView, BlogDetailView

urlpatterns = [
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/<int:pk>/<slug:slug>/", BlogDetailView.as_view(), name="post_detail"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
