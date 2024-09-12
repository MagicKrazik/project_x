from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('media/', views.media, name='media'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('meeting/', views.meeting, name='meeting'),
    path('prices/', views.prices, name='prices'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

]