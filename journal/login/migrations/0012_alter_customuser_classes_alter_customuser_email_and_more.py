# Generated by Django 4.1.4 on 2023-03-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_rename_is_confirmed_customuser_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='classes',
            field=models.CharField(blank=True, default='', help_text='Класс для ученика или классы, которые обучает учитель, если много, пишется через пробел', max_length=254, verbose_name='классы'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='father_name',
            field=models.CharField(blank=True, default='', help_text='Если отчества нет, оставьте поле пустым', max_length=254, verbose_name='отчество'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_email_verified',
            field=models.BooleanField(default=False, verbose_name='подтверждённый'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(default=False, help_text='Отметье, если пользователь считается учителем', verbose_name='учитель'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='subjects',
            field=models.CharField(blank=True, default='', help_text='Предметы, которые преподаёт учитель, если ученик - оставить пустым', max_length=254, verbose_name='предметы'),
        ),
    ]
