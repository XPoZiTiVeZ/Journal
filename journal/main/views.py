from django.shortcuts import render, redirect
from .models import Mark
from .forms import MarkForm
from datetime import date, timedelta, datetime

# Create your views here.

def index(request):
    marks = Mark.objects.order_by('title')
    start = datetime.strptime('1/1/2022', '%d/%m/%Y')
    end = datetime.strptime('1/1/2024', '%d/%m/%Y')   
    daterange = [(start + timedelta(days=x)).strftime('%d/%a') for x in range(0, (end-start).days)]
    return render(request, 'main/index.html', {'title' : 'Главная страница дневника', 'marks' : marks, 'range':daterange})

def about(request):
    return render(request, 'main/about.html')

def addmark(request):
    error = ''
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была заполнена неправильно'

    form = MarkForm()
    context = {
        'form' : form,
        'error' : error,
    }
    return render(request, 'main/addmark.html', context)