from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login.html', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout.html', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register.html', views.register, name='register'),
    path('profile.html', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



