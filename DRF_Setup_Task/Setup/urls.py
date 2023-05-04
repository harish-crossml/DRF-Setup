from django.urls import path
from django.conf import urls
from . import views
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/detail/<str:pk>/', HomeDetailView.as_view(), name='detail-home'),
    path('api/<str:pk>/', HomeView.as_view(), name='create-home'),
]