# Generated by Django 4.1.4 on 2023-01-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='customuser',
            name='father_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='father name'),
        ),
    ]
