from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_view, name='list'),
    path('register', views.register_view, name='register'),
    path('download-excel/', views.download_excel, name='download_excel'),
]