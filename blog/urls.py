from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView, \
    toggle_visibility, BlogEditListView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/edit/', BlogEditListView.as_view(), name='blog_edit'),
    path('blog/create/', BlogCreateView.as_view(), name='create'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('blog/view/<slug:slug>', BlogDetailView.as_view(), name='view'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('blog/visibility/<int:pk>', toggle_visibility, name='toggle_visibility'),
]
