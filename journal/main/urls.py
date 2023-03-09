from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .models import


urlpatterns = [
    path('', views.index, name='home'),
    path('diary', views.diary, name='diary'),
    path('tasks', views.tasks, name='tasks'),
    path('marks', views.marks, name='marks'),
    path('about', views.about, name='about'),
    path('addmark', views.addmark, name='add-mark'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)