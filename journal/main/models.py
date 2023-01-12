from django.db import models

# Create your models here.

class Mark(models.Model):
    title = models.CharField('Предмет', max_length=50)
    mark = models.IntegerField('Оценка')
    date = models.DateField('Дата')
    class MarkType(models.TextChoices):
        homew = 1, 'Домашняя работа'
        classw = 2, 'Классная работа'
        selfw = 3, 'Самостоятельная работа'
        controlw = 4, 'Контрольная работа'
        acontrolw = 5, 'Административная контрольная работа'
    marktype = models.CharField('Описание', max_length = 50, choices=MarkType.choices, default=MarkType.classw)

    def __str__(self):
        return str(self.title) + ' ' + str(self.mark) + ' ' + str(self.date)
    
    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

class Work(models.Model):
    title = models.CharField('Предмет', max_length=50)
    work = models.IntegerField('Оценка')
    date = models.DateField('Дата')

    def __str__(self):
        return str(self.title) + ' ' + str(self.mark) + ' ' + str(self.date)
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
