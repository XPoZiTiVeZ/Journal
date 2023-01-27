from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# class CustomUser(AbstractUser):
#     email = models.CharField(_("email address"), max_length=254, unique=True)
#     father_name = models.CharField(_("father name"), max_length=150, blank=True)
#     is_teacher = models.BooleanField(default=False)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Почта'), unique=True)
    father_name = models.CharField(_('Отчество'), max_length=254, blank=True, help_text='Если отчества нет, оставьте поле пустым')
    is_confirmed = models.BooleanField(_('Подтверждённый'), default=False)
    is_teacher = models.BooleanField(_('Учитель'), default=False, help_text='Отметье, если пользователь считается учителем')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username} профиль'