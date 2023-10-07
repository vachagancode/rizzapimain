from django.urls import path
from . import views

app_name = 'rizz'

urlpatterns = [
    path('rizz/api/get/', views.getData),
    path('rizz/api/add/', views.addData),
    path('rizz/add/', views.add_rizz, name='add')
]