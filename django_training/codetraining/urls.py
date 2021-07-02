from django.urls import path
from codetraining import views

urlpatterns = [
    path('', views.home, name='home'),
]