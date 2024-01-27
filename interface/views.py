from django.shortcuts import render
from api_components import API_INTERFACE

# Creating an object of the API_INFERENCE class, so that 
# we don't need to create this object again and again in the view functions

interface = API_INTERFACE()


# renders the home page 
def home(request):

    return render(request, 'home.html')

#  renders the page for Realtime currency exchange , utilises the function CURRENCY_EXCHANGE_RATE 
# When the form is submitted rendered in the websits, it sends a POST request to this function, 
# The send values are then used to call corresponding instances from the interface object
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

#  renders the page for Realtime currency exchange , utilises the function FX_INTRADAY 
# When the form is submitted rendered in the websits, it sends a POST request to this function, 
# The send values are then used to call corresponding instances from the interface object
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

#  renders the page for Realtime currency exchange , utilises the function FX_DAILY 
# When the form is submitted rendered in the websits, it sends a POST request to this function, 
# The send values are then used to call corresponding instances from the interface object
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

#  renders the page for Realtime currency exchange , utilises the function FX_WEEKLY 
# When the form is submitted rendered in the websits, it sends a POST request to this function, 
# The send values are then used to call corresponding instances from the interface object
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

#  renders the page for Realtime currency exchange , utilises the function FX_MONTHLY 
# When the form is submitted rendered in the websits, it sends a POST request to this function, 
# The send values are then used to call corresponding instances from the interface object
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
