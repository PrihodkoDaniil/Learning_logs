"""Определяет схемы URL для learning_lods."""

from django.urls import path
from . import views

app_name = 'learning_lods'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
