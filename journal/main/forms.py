from .models import Mark
from django.forms import ModelForm, TextInput, Select
from datetime import datetime, date

class MarkForm(ModelForm):  
    class Meta:
        model = Mark
        fields = ['title', 'mark', 'marktype', 'date']
        choicestitle = (('Русский язык', 'Русский язык'),('Алгебра', 'Алгебра'),('Геометрия', 'Геометрия'))
        choicesmark = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
        choicesmarktype = (('Домашняя работа', 'Домашняя работа'), ('Классная работа', 'Классная работа'), ('Самостоятельная работа', 'Самостоятельная работа'), ('Контрольная работа', 'Контрольная работа'), ('Административная контрольная работа', 'Административная контрольная работа'))
        widgets = {
            'title' : Select(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите предмет',
            }, choices = choicestitle),
            'mark' : Select(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите предмет',
            }, choices = choicesmark),
            'marktype' : Select(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите предмет',
            }, choices = choicesmarktype),
            'date' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите дату',
                'type' : 'date',
                'value' : datetime.now().strftime('%Y-%m-%d')
            })
        }
        print(datetime.now().strftime('%Y-%m-%d'), 123)