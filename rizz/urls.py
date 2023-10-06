from django.urls import path
from . import views

app_name = 'rizz'

urlpatterns = [
    path('api/get/', views.getData),
    path('api/add', views.addData),
    path('add/', views.add_rizz, name='add')
]