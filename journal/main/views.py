from django.shortcuts import render, redirect
from .models import Mark, Task
from .forms import MarkForm
from django.views.generic import TemplateView
from datetime import date, timedelta, datetime
from django.conf import settings
import locale
import json
import os
locale.setlocale(locale.LC_ALL, '')

startday = datetime.strptime('1/1/2023', '%d/%m/%Y')
endday = datetime.strptime('1/1/2024', '%d/%m/%Y')

def m(month):
    if month == "Март" or month == "Август":
        return month.lower() + "а"
    return month[:-1].lower() + "я"

def read():
    filepath = os.path.join(settings.STATIC_ROOT, 'diary.json')
    with open(filepath, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data

def index(request):
    return render(request, 'main/index.html')

def diary(request):
    if not request.GET.get('date'):
        date = datetime.now().strftime('%d/%m/%Y')
    else:
        date = request.GET.get('date')

    startweek = datetime.strptime(f'Пн/{datetime.strptime(date, "%d/%m/%Y").strftime("%W/%Y")}', '%a/%W/%Y')

    nowday = datetime.now().strftime('%#d')
    day = datetime.strptime(date, '%d/%m/%Y').strftime('%A').capitalize()
    month = m(datetime.strptime(date, '%d/%m/%Y').strftime('%B'))
    dateinfo = (datetime.strptime(date, '%d/%m/%Y').strftime('%a'), datetime.strptime(date, '%d/%m/%Y').strftime('%#d'), datetime.strptime(date, '%d/%m/%Y').strftime(f'{day}, %#d {month}'))
    info = [[f"{(startweek + timedelta(days = x)).strftime('%A, %#d').title()} {m((startweek + timedelta(days = x)).strftime('%B'))}", (startweek + timedelta(days = x)).strftime('%#d')] for x in range(6)]

    diary = read() 

    for i, key in enumerate(diary.get("lsn").keys()):
        lessons = []
        intervals = [10, 20, 20, 10, 30, 20, 10, 0]
        min = 510
        for j, val in enumerate(diary.get("lsn").get(key).values()):
            nmin = min + 45
            lessons.append((f"{j+1} урок {min//60}:{min%60} - {nmin//60}:{nmin%60} {'каб. ' + val[1] if val[1] else ''}", val[0]))
            min = nmin + intervals[j]
        info[i].append(lessons)   

    tasks = [(Task.objects.filter(date = (startweek + timedelta(days = x)).strftime('%Y-%m-%d'))) for x in range(6)]

    for i, task in enumerate(tasks):
        taskinfos = []
        for taskinfo in task:
            taskinfos.append((taskinfo.title, taskinfo.shortdesk))
        info[i].append(taskinfos) 
    
    marks = [(Mark.objects.filter(date = (startweek + timedelta(days = x)).strftime('%Y-%m-%d'))) for x in range(6)]

    for i, mark in enumerate(marks):
        markinfos = []
        for markinfo in mark:
            if markinfo.marktype == '1' or markinfo.marktype == '2' or markinfo.marktype == '3':
                marktype = 1
            elif markinfo.marktype == '4':
                marktype = 2
            elif markinfo.marktype == '5':
                marktype = 3
            else:
                marktype = 1
            markinfos.append((markinfo.title, markinfo.mark, marktype))
        info[i].append(markinfos)

    try:
        asa = list(diary["asa"][dateinfo[0]].values())
    except:
        asa = ["Нет дополнительных занятий"]
    excdate = list(diary["exc"].keys())
    exc = list(diary["exc"].values())
    return render(request, 'main/diary.html', {'title' : 'Главная страница дневника', 'info':info, 'day':nowday})


def tasks(request):
    mark = Task.objects.all().order_by('title')
    marks = []
    for markinfo in mark:
        if markinfo.marktype == '1' or markinfo.marktype == '2' or markinfo.marktype == '3':
            marktype = ""
        elif markinfo.marktype == '4':
            marktype = 2
        elif markinfo.marktype == '5':
            marktype = 3
        else:
            marktype = ""
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
    return render(request, 'main/tasks.html', {'title' : 'Главная страница дневника', 'daterange':daterange, 'day':startday, 'datenow':now, 'nowmonth':nowmonth, 'date':date, 'marks':marks})

def marks(request):
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
    return render(request, 'main/marks.html', {'title' : 'Главная страница дневника', 'daterange':daterange, 'day':startday, 'datenow':now, 'nowmonth':nowmonth, 'date':date, 'marks':marks})

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
