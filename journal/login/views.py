from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


from django.views import View
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def login(request):
    return render(request, 'login/login.html')

def register(request):
    form = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_unusable_password()
            user.save()
            messages.success(request, 'Создан аккаунт!')
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'login/profile.html')