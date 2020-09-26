from django.urls import path

from . import views

urlpatterns = [
    path('getall/', views.getall, name='getall')
]
