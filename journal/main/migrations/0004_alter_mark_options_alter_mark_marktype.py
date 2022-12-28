# Generated by Django 4.1.4 on 2022-12-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mark_marktype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterField(
            model_name='mark',
            name='marktype',
            field=models.CharField(choices=[('1', 'Домашняя работа'), ('2', 'Классная работа'), ('3', 'Самостоятельная работа'), ('4', 'Контрольная работа'), ('5', 'Административная контрольная работа')], default='2', max_length=50, verbose_name='Описание'),
        ),
    ]
