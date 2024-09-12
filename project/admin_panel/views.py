from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from website.models import CustomUser  # Make sure this import is correct

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = CustomUser.objects.count()
    active_users = CustomUser.objects.filter(is_active=True).count()
    estimated_profit = (total_users * 250)  # Calculating estimated profit
    recent_activity = CustomUser.objects.order_by('-date_joined')[:5]
    
    context = {
        'total_users': total_users,
        'active_users': active_users,
        'estimated_profit': estimated_profit,
        'recent_activity': recent_activity,
    }
    
    return render(request, 'admin_panel/dashboard.html', context)

@user_passes_test(is_admin)
def manage_users(request):
    users = CustomUser.objects.all().order_by('-date_joined')
    
    context = {
        'users': users,
    }
    
    return render(request, 'admin_panel/manage_users.html', context)