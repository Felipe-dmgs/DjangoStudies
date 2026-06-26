from django.urls import path
from . import views

urlpatterns = [
# Quando a URL for a raiz (''), chame a função 'home' de 'views.py'
path('', views.home, name='home'),
]
