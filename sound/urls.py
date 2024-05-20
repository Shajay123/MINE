# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('contacts/', views.contact_list, name='contact_list'),
]
