from django.urls import path
from .views import newsList,newsDetail


urlpatterns = [
    path('news-list/',newsList),
    path('news-detail/<int:id>/',newsDetail)
]