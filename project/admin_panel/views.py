from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from website.models import CustomUser
from django.core.paginator import Paginator
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_protect
from datetime import timedelta
from django.utils import timezone
from website.models import PhotographerAvailability
from django import forms
from django.contrib import messages



def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = CustomUser.objects.filter(is_staff=False).count()
    active_users = CustomUser.objects.filter(is_staff=False, is_active=True).count()
    estimated_profit = active_users * 250  # Assuming $250 per active user
    recent_activity = CustomUser.objects.filter(is_staff=False).order_by('-date_joined')[:5]
    
    context = {
        'total_users': total_users,
        'active_users': active_users,
        'estimated_profit': estimated_profit,
        'recent_activity': recent_activity,
    }
    
    return render(request, 'admin_panel/dashboard.html', context)

@user_passes_test(is_admin)
def manage_users(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', 'all')
    
    users = CustomUser.objects.filter(is_staff=False)
    
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(phone_number__icontains=search_query)
        )
    
    if status_filter == 'active':
        users = users.filter(is_active=True)
    elif status_filter == 'inactive':
        users = users.filter(is_active=False)
    
    users = users.order_by('-date_joined')
    
    # Calculate renewal date and days left for each user
    today = timezone.now().date()
    for user in users:
        if user.activation_date:
            user.renewal_date = user.activation_date + timedelta(days=30)
            if user.is_active:
                user.days_left = (user.renewal_date.date() - today).days
            else:
                user.days_left = None
        else:
            user.renewal_date = None
            user.days_left = None
    
    paginator = Paginator(users, 20)  # Show 20 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
    }
    
    return render(request, 'admin_panel/manage_users.html', context)

@user_passes_test(is_admin)
@require_POST
@csrf_protect
def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, is_staff=False)
    user.activate()
    
    # Add user to the appropriate group (if needed)
    customer_group, created = Group.objects.get_or_create(name='Customers')
    user.groups.add(customer_group)
    
    return JsonResponse({
        'success': True, 
        'message': f'User {user.username} has been activated.',
        'activation_date': user.activation_date.strftime('%d/%m/%Y'),
        'renewal_date': (user.activation_date + timedelta(days=30)).strftime('%d/%m/%Y'),
        'days_left': '30'
    })

@user_passes_test(is_admin)
@require_POST
@csrf_protect
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, is_staff=False)
    user.deactivate()
    
    # Remove user from the customer group (if needed)
    customer_group = Group.objects.filter(name='Customers').first()
    if customer_group:
        user.groups.remove(customer_group)
    
    return JsonResponse({'success': True, 'message': f'User {user.username} has been deactivated.'})


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = PhotographerAvailability
        fields = ['date', 'start_time', 'end_time', 'is_available']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

@user_passes_test(lambda u: u.is_staff)
def manage_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Availability added successfully.')
            return redirect('manage_availability')
    else:
        form = AvailabilityForm()
    
    availabilities = PhotographerAvailability.objects.all().order_by('date', 'start_time')
    
    context = {
        'form': form,
        'availabilities': availabilities,
    }
    return render(request, 'admin_panel/manage_availability.html', context)

@user_passes_test(lambda u: u.is_staff)
def delete_availability(request, availability_id):
    availability = PhotographerAvailability.objects.get(id=availability_id)
    availability.delete()
    messages.success(request, 'Availability deleted successfully.')
    return redirect('manage_availability')