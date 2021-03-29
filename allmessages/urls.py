from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<link>/', views.update, name='update'),
    path('list/<link>/', views.lists, name='lists'),
    path('single/<link>/', views.single, name='single')
]
