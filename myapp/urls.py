from django.urls import path

from . import views


urlpatterns = [
     
     path('', views.index,name="index"),
     path('contact/', views.contact,name="contact"),
     path('topics-detail/', views.topics_detail,name="topics-detail"),
     path('topics-listing/', views.topics_listing,name="topics-listing"),
]