from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list, name='reviews_list'),
    path('create/', views.create_review, name='create_review'),
    path('edit/<int:id>/', views.edit_review, name='edit_review'),
    path('delete/<int:id>/', views.delete_review, name='delete_review'),
]