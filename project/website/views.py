from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import RegistrationForm
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
import os
from django.utils import timezone
from .models import CustomUser, Membership


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User starts inactive until payment is confirmed
            user.save()
            messages.success(request, 'Registro exitoso. Por favor, realiza el depósito bancario para activar tu cuenta.')
            return redirect('home')
    else:
        form = RegistrationForm()
    
    membership = Membership.objects.first()
    return render(request, 'register.html', {'form': form, 'membership': membership})

def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    
    users = CustomUser.objects.all()
    context = {
        'total_users': users.count(),
        'active_users': users.filter(is_active=True).count(),
        'pending_users': users.filter(payment_status='pending').count(),
        'overdue_users': users.filter(payment_status='overdue').count(),
    }
    return render(request, 'admin/dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the members page
        else:
            messages.error(request, 'Nombre de usuario o contraseña inválidos')
    return render(request, 'login.html')

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        try:
            user.delete()
            messages.success(request, 'Tu cuenta ha sido eliminada exitosamente.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Hubo un error al eliminar tu cuenta: {str(e)}')
            return redirect('profile')
    else:
        return render(request, 'confirm_delete.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente')
    return redirect('home')  # Redirect to the home page after logout

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def media(request):
    return render(request, 'media.html')

@login_required
def meeting(request):
    return render(request, 'meeting.html')

@login_required
def prices(request):
    return render(request, 'prices.html')



########### Unfinished ###########



def media_view(request):
    # Path to the images directory
    images_dir = os.path.join(settings.STATIC_ROOT, 'images')

    # Get all folders in the images directory
    folders = []
    for item in os.listdir(images_dir):
        item_path = os.path.join(images_dir, item)
        if os.path.isdir(item_path):
            # Get the first image in the folder to use as a thumbnail
            thumbnail = next((f for f in os.listdir(item_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))), None)
            folders.append({
                'name': item,
                'thumbnail': os.path.join(item, thumbnail) if thumbnail else 'folder-icon.png'
            })

    # Sample data structure for videos (you might want to adjust this based on your needs)
    videos = [
        {'title': 'Detrás de Cámaras: Sesión de Fotos', 'thumbnail': 'video-thumbnail-1.jpg'},
        {'title': 'Tutorial de Maquillaje', 'thumbnail': 'video-thumbnail-2.jpg'},
        {'title': 'Vlog: Un Día en Mi Vida', 'thumbnail': 'video-thumbnail-3.jpg'},
    ]

    context = {
        'folders': folders,
        'videos': videos,
    }

    return render(request, 'media.html', context)



def get_folder_images(request, folder_name):
    folder_path = os.path.join(settings.STATIC_ROOT, 'images', folder_name)
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return JsonResponse({'images': images})