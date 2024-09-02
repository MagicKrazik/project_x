from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            return function(request, *args, **kwargs)
        return redirect('admin_login')
    return wrap