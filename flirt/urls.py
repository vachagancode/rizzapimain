from django.urls import path
from . import views

app_name = 'flirt'

urlpatterns = [
    path('get/flirt/', views.getData),
    path('post/flirt/', views.postData),
    path('add_flirt/', views.add_flirt, name='add_flirt')
]