from django.urls import path

from QuickRow import views

urlpatterns = [
    path('', views.index, name='index')
]
