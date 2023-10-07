from django.urls import path
from . import views

app_name = 'eusers'

urlpatterns = [
    path('api/get/', views.getData),
    path('api/post/', views.addData),
]