# Generated by Django 4.1.4 on 2023-01-14 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_work_work_work_fullwork_work_shortwork'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Work',
            new_name='Task',
        ),
    ]