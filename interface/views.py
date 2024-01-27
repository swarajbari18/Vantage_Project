from django.shortcuts import render, HttpResponse
from api_components import API_INTERFACE

interface = API_INTERFACE()



def home(request):

    return render(request, 'home.html')


def realtime(request):
    data = None
    if request.method == 'POST':
        from_currency = request.POST.get('from')
        to_currency = request.POST.get('to')
        data = interface.get_current_ex(
            from_currency= from_currency,
            to_currency= to_currency
        )
    return render(request, 'realtime.html', data)


def interval(request):
    data = None
    if request.method == 'POST':
        from_currency = request.POST.get('from')
        to_currency = request.POST.get('to')
        interval = request.POST.get('interval')
        data = interface.get_intraday_ex(
            from_symbol= from_currency,
            to_symbol= to_currency,
            interval= interval
        )
    return render(request, 'interval.html', data)


def daily(request):
    data = None
    if request.method == 'POST':
        from_currency = request.POST.get('from')
        to_currency = request.POST.get('to')
        data = interface.get_daily_ex(
            from_symbol= from_currency,
            to_symbol= to_currency
        )

    return render(request, 'daily.html', data)


def weekly(request):
    data = None
    if request.method == 'POST':
        from_currency = request.POST.get('from')
        to_currency = request.POST.get('to')
        data = interface.get_weekly_ex(
            from_symbol= from_currency,
            to_symbol= to_currency
        )
    return render(request, 'weekly.html', data)


def monthly(request):
    data = None
    if request.method == 'POST':
        from_currency = request.POST.get('from')
        to_currency = request.POST.get('to')
        data = interface.get_monthly_ex(
            from_symbol= from_currency,
            to_symbol= to_currency
        )
    return render(request, 'monthly.html', data)
