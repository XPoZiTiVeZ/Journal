from django.urls import path
from . import views
from login import views as login_views
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime

urlpatterns = [
    path('', views.index, name='main'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('addmark', views.addmark, name='add-mark'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)