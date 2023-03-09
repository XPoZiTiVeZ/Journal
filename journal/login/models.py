from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('почта'), unique=True)
    father_name = models.CharField(_('отчество'), max_length=254, blank=True, help_text='Если отчества нет, оставьте поле пустым', default="")
    classes = models.CharField(_('классы'), max_length=254, blank=True, help_text="Класс для ученика или классы, которые обучает учитель, если много, пишется через пробел", default="")
    subjects = models.CharField(_('предметы'), max_length=254, blank=True, help_text="Предметы, которые преподаёт учитель, если ученик - оставить пустым", default="")
    is_email_verified = models.BooleanField(_('подтверждённый'), default=False)
    is_teacher = models.BooleanField(_('учитель'), default=False, help_text='Отметье, если пользователь считается учителем')
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