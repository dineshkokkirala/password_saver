from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('hide/', views.hide, name='hide'),
    path('hide/<int:id>', views.delete, name='delete'),
    path('hide/update/<int:id>/<str:val>', views.update, name='update'),
]
