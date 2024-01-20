from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView, \
    toggle_visibility, BlogEditListView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', never_cache(BlogListView.as_view()), name='blog'),
    path('blog/edit/', never_cache(BlogEditListView.as_view()), name='blog_edit'),
    path('blog/create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('blog/edit/<int:pk>', never_cache(BlogUpdateView.as_view()), name='update'),
    path('blog/view/<slug:slug>', never_cache(BlogDetailView.as_view()), name='view'),
    path('blog/delete/<int:pk>', never_cache(BlogDeleteView.as_view()), name='delete'),
    path('blog/visibility/<int:pk>', toggle_visibility, name='toggle_visibility'),
]
