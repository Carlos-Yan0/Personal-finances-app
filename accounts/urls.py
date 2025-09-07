from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forgotPassword/',views.forgotPassword, name='forgotPassword'),
    path('signup', views.signup, name='signup'),
]