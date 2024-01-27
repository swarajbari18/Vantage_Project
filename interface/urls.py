from django.contrib import admin
from django.urls import path
from interface import views

'''
By default the HomePage will open, 
After clicking on the buttons, subsequent page will open up,
For that to happen we need a different path for each functional API endpoin, 
these are the url  patterns for that 
'''
urlpatterns = [
    path('', views.home, name= 'HomePage'),
    path('realtime', views.realtime, name= 'Realtime Exchange Rate'),
    path('interval', views.interval, name= 'Intraday Exchange Rate'),
    path('daily', views.daily, name= 'Daily Exchange Rate'),
    path('weekly', views.weekly, name= 'Weeklyy Exchange Rate'),
    path('monthly', views.monthly, name= 'Monthly Exchange Rate'),
]
