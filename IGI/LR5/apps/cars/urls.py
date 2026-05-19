from django.urls import path

from . import views

urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('create/', views.create_car, name='create_car'),
    path('edit/<int:id>/', views.edit_car, name='edit_car'),
    path('delete/<int:id>/', views.delete_car, name='delete_car'),
]