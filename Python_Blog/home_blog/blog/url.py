from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='home_blog'),
    path('blog_post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog_post/new/', PostCreateView.as_view(), name='post_create'),
    path('blog_post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('blog_post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)