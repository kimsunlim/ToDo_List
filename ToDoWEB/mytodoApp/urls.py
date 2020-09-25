from django.contrib import admin
from django.urls import path,include
from mytodoApp import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('createTodo/', views.createTodo,name='createTodo'),
    path('deleteTodo/', views.doneTodo,name='deleteTodo'),
]