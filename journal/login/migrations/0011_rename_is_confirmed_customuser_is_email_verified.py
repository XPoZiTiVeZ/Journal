# Generated by Django 4.1.4 on 2023-03-05 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_customuser_classes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_confirmed',
            new_name='is_email_verified',
        ),
    ]