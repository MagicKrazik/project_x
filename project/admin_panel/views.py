from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .decorators import admin_required

def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error_message = "Invalid credentials or insufficient permissions."
            return render(request, 'admin_panel/login.html', {'error_message': error_message})
    return render(request, 'admin_panel/login.html')

@admin_required
def admin_dashboard(request):
    return render(request, 'admin_panel/dashboard.html')