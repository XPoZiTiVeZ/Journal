from django.urls import path
from . import views
from login import views as login_views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('addmark', views.addmark, name='add-mark'),
]