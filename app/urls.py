from . import views
from django.urls import path

urlpatterns = [
    path('', views.app, name = 'app'),
    path('send', views.send, name = 'send'),
]