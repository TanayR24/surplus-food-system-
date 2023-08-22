from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('ABC001', views.profile, name='ABC001'),
]

