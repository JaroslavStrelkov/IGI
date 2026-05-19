from django.shortcuts import render
from .models import (AboutCompany, News, FAQ, EmployeeContact, Vacancy)
from django.utils import timezone
import calendar
import requests

def about_page(request):
    company = AboutCompany.objects.first()

    return render(request, 'pages/about.html', {'company': company})

def news_list(request):
    news = News.objects.all().order_by('-created_at')

    return render(request, 'pages/news.html', {'news': news})

def faq_page(request):
    faqs = FAQ.objects.all()

    return render(request, 'pages/faq.html', {'faqs': faqs})

def contacts_page(request):
    contacts = EmployeeContact.objects.all()

    return render(request, 'pages/contacts.html', {'contacts': contacts})

def vacancies_page(request):
    vacancies = Vacancy.objects.all()

    return render(request, 'pages/vacancies.html', {'vacancies': vacancies})


def privacy_page(request):
    return render(request, 'pages/privacy.html')

def external_api_page(request):
    btc_data = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR').json()
    dog_image = None

    if request.user.is_authenticated:
        dog_data = requests.get('https://dog.ceo/api/breeds/image/random').json()
        dog_image = dog_data['message']

    context = {'btc_price': (btc_data['price']), 'dog_image': dog_image,}

    return render(request, 'pages/external_api.html', context)

def timezone_page(request):
    utc_time = timezone.now()
    local_time = timezone.localtime(utc_time)
    current_year = local_time.year
    current_month = local_time.month
    text_calendar = calendar.month(current_year,current_month)
    context = {'utc_time': utc_time, 'local_time': local_time, 'calendar': text_calendar,}

    return render(request, 'pages/timezone.html', context) 
