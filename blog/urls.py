from django.urls import path
from . import views
from .views import PostDetailView, PostListView, PostCreatView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new', PostCreatView.as_view(), name='post-create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about')
]