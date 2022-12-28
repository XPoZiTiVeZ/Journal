from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def login(request):
    return render(request, 'login/login.html')

def register(request):
    form = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'login/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'login/profile.html')