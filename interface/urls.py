from django.contrib import admin
from django.urls import path
from interface import views


urlpatterns = [
    path('', views.home, name= 'HomePage'),
    path('realtime', views.realtime, name= 'Realtime Exchange Rate'),
    path('interval', views.interval, name= 'Intraday Exchange Rate'),
    path('daily', views.daily, name= 'Daily Exchange Rate'),
    path('weekly', views.weekly, name= 'Weeklyy Exchange Rate'),
    path('monthly', views.monthly, name= 'Monthly Exchange Rate'),
]
