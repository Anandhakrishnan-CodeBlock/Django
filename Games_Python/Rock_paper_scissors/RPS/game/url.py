from django.urls import path
from .views import ScoreListView
from .import views

urlpatterns = [
    path('', ScoreListView.as_view(), name='index'),
    path('start', views.start, name='start'),

]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
