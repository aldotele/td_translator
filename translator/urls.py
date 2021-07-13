from django.contrib import admin
from django.urls import path, include
from translator.views import home, translate

urlpatterns = [
    path('', home, name='home'),  # new
    path('result/', translate, name='result'),

    path('lang/<slug:slug>/', home, name='home_eng'),
]

