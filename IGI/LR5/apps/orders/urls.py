from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_list, name='orders_list'),
    path('create/', views.create_order, name='create_order'),
    path('edit/<int:id>/', views.edit_order, name='edit_order'),
    path('take/<int:id>/', views.take_order, name='take_order'),
    path('delete/<int:id>/', views.delete_order, name='delete_order'),
    path('status/int:id/str:status/', views.change_status, name='change_status'),
]