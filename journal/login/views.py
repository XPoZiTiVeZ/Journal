from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .backends import CustomBackend as CB
from .forms import CustomCreationForm
from .models import CustomUser
from .utils import generate_token

from django.views import View
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from validate_email import validate_email
import smtplib

def send_verification_email(request, user):
    current_site = get_current_site(request)
    email_subject = 'Верификация аккаунта'
    email_body = render_to_string('login/verification.html', {
        'user': user.email,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user),
    })
    email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_FROM_USER, to=[user.email])
    email.send()

def login_user(request):
    if request.method == "POST":
        context = {'data': request.POST}
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CB.authenticate(request, username=email, password=password)

        if user and not user.is_email_verified:
            messages.add_message(request, messages.ERROR,
                                 'Почта не подтверждена, пожалуйста проверьте почту')
            return render(request, 'login/login.html', context)
        
        if user and not user.is_active:
            messages.add_message(request, messages.ERROR,
                                 'Аккаунт ещё не подтверждён администратором, если вы считаете, что это ошибка, напишите в тех. поддержку')
            return render(request, 'login/login.html', context)

        if not user:
            messages.add_message(request, messages.ERROR, 'Неправильная почта или пароль')
            return render(request, 'login/login.html', context)
    
        login(request, user)

        messages.add_message(request, messages.SUCCESS, f'Доброй пожаловать, {user.last_name} {user.first_name}')
        return redirect('diary')
    return render(request, 'login/login.html')

def register(request):
    if request.method == 'POST':
        context = {'has_error': False, 'data': request.POST}
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
    
        if len(password) < 8:
            messages.add_message(request, messages.ERROR,
                                 'Пароль должен быть больше 8 символов')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Пароли не совпадают')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Введена недействительная почта')
            context['has_error'] = True

        if not email:
            messages.add_message(request, messages.ERROR,
                                 'Почта не введена')
            context['has_error'] = True

        if CustomUser.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Такая почта уже зарегистрирована')
            context['has_error'] = True
            return render(request, 'login/register.html', context)

        if context['has_error']:
            return render(request, 'login/register.html', context)
        
        user = CustomUser.objects.create_user(email=email, password=password)
        user.is_active = False
        user.last_name = last_name
        user.first_name = first_name
        user.save()

        if not context['has_error']:
            send_verification_email(request, user)
            messages.add_message(request, messages.SUCCESS, 'Верифицируйте аккаунт, перейдя по ссылке из почты, чтобы продолжить')
            return redirect('login')
        
    return render(request, 'login/register.html')

def verificate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        
        messages.add_message(request, messages.SUCCESS, 'Вы успешно подтвердили аккаунт, ожидайте подтверждения от администратора')
        return redirect('login')
    
    return render(request, 'login/verification-failed.html', {'user':user})

@login_required
def profile(request):
    return render(request, 'login/profile.html')