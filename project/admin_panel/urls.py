from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # Add more URL patterns for other admin views
]