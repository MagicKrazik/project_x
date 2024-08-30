from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegistrationForm
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            # For example, create a new user
            # Then redirect to a new URL:
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


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