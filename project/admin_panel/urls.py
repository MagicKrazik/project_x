from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-users/activate/<int:user_id>/', views.activate_user, name='activate_user'),
    path('manage-users/deactivate/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('manage-availability/', views.manage_availability, name='manage_availability'),
    path('delete-availability/<int:availability_id>/', views.delete_availability, name='delete_availability'),
    # Add more URL patterns for other admin views
]