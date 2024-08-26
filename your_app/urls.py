"""Defines URL patterns for your_app app"""

from django.urls import path

from . import views

app_name = 'your_app'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Home Page again with optional parm, I don't believe in esoteric code (regex)
    path('<slug:option>', views.index, name='index'),
]
