from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='myblog_home'),
    path('about/', views.about, name='myblog_about'),
]
