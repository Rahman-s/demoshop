from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shoe/<int:pk>/', views.shoe_detail, name='shoe_detail'),
]