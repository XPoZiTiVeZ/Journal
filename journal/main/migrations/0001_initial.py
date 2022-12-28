# Generated by Django 4.1.4 on 2022-12-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Предмет')),
                ('mark', models.IntegerField(verbose_name='Оценка')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
        ),
    ]