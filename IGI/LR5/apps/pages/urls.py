from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('news/', views.news_list, name='news'),
    path('faq/', views.faq_page, name='faq'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('vacancies/', views.vacancies_page, name='vacancies'),
    path('privacy/', views.privacy_page, name='privacy'),
    path('external-api/', views.external_api_page, name='external_api'),
    path('timezone/', views.timezone_page, name='timezone'),
]