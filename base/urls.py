from django.urls import path
from .views import index, redirect_url, generate_url


urlpatterns = [
    path('', index, name='index'),
    path('<str:code>', redirect_url, name='redirect'),
    path('generate_url', generate_url, name='generate_url'),
]
