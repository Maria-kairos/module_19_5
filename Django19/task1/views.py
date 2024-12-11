from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
users = ['user1', 'user2', 'user3']

def news(request):
    posts = News.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fifth_task/news.html', {'page_obj': page_obj})

def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            existing_users = Buyer.objects.values_list('name', flat=True)

            if username in existing_users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                info['message'] = f'Приветствуем, {username}!'

        info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        existing_users = Buyer.objects.values_list('name', flat=True)

        if username in existing_users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=username, age=age, balance=1000)
            info['message'] = f'Приветствуем, {username}!'

    return render(request, 'fifth_task/registration_page.html', info)

def get_all_users():
    return Buyer.objects.all().values_list('name', flat=True)

def t3(request):
    title = 'Title'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/t3.html', context)

def magazin(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'fourth_task/magazin.html', context)

def korzina(request):
    title = 'Title'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/korzina.html', context)
# Create your views here.
