from django.shortcuts import render, redirect
from .models import Mark
from .forms import MarkForm
from django.views.generic import TemplateView
from datetime import date, timedelta, datetime
import locale
locale.setlocale(locale.LC_ALL, '')

def index(request):
    return render(request, 'main/index.html')

def home(request):
    mark = Mark.objects.all().order_by('title')
    marks = []
    for markinfo in mark:
        if markinfo.marktype == '1' or markinfo.marktype == '2' or markinfo.marktype == '3':
            marktype = 1
        elif markinfo.marktype == '4':
            marktype = 2
        elif markinfo.marktype == '5':
            marktype = 3
        else:
            marktype = 1
        marks.append((markinfo.title, markinfo.mark, marktype, markinfo.date.strftime('%d/%m/%Y')))

    if not request.GET.get('date'):
        date = datetime.now().strftime('%d/%m/%Y')
    else:
        date = request.GET.get('date')
    start = '1/1/2023'
    end = '1/1/2024'
    startday = datetime.strptime(start, '%d/%m/%Y')
    while startday.strftime('%a') != 'Пн':
        startday = startday + timedelta(days=1)
    endday = datetime.strptime(end, '%d/%m/%Y')
    now = (datetime.strptime(date, '%d/%m/%Y') - datetime.strptime(start, '%d/%m/%Y')).days
    if datetime.strptime(date, '%d/%m/%Y').strftime('%a') == 'Пт' or datetime.strptime(date, '%d/%m/%Y').strftime('%a') == 'Сб' or datetime.strptime(date, '%d/%m/%Y').strftime('%a') == 'Вс':
        now -= 3
    nowmonth = datetime.now().strftime('%B')
    daterange = [((startday + timedelta(days=x)).strftime('%d %a'), (startday + timedelta(days=x)).strftime('%B'), (startday + timedelta(days=x)).strftime('%d/%m/%Y')) for x in range(0, (endday-startday).days)]
    return render(request, 'main/main.html', {'title' : 'Главная страница дневника', 'daterange':daterange, 'day':startday, 'datenow':now, 'nowmonth':nowmonth, 'date':date, 'marks':marks})

def about(request):
    return render(request, 'main/about.html')

def addmark(request):
    error = ''
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была заполнена неправильно'

    form = MarkForm()
    context = {
        'form' : form,
        'error' : error,
    }
    return render(request, 'main/addmark.html', context)
