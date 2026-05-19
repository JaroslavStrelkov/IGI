from django.urls import path

from . import views

urlpatterns = [
    path('', views.promo_list, name='promo_list'),
    path('create/', views.create_promo, name='create_promo'),
    path('edit/<int:id>/', views.edit_promo, name='edit_promo'),
    path('delete/<int:id>/', views.delete_promo, name='delete_promo'),
]