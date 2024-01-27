import requests
import pandas as pd
from Forex_endpoint.settings import API_KEY



class API_INTERFACE:

    def __init__(self, API_KEY= API_KEY) -> None:
        self.url_head = 'https://www.alphavantage.co/query?'
        self.API_KEY = API_KEY

    def _get_url(self, *args):
        return self.url_head + '&'.join(args) + f'&apikey={self.API_KEY}'

    def _get_response(self, url, key):
        r = requests.get(url)
        data = r.json()[key]
        if key == 'Realtime Currency Exchange Rate':
            data = pd.DataFrame([data]).T.to_html()
        else:    
            data = pd.DataFrame(data).T.to_html()
        return {'html_table': data}

    def get_current_ex(self, from_currency, to_currency):
        function= 'CURRENCY_EXCHANGE_RATE'
        url = self._get_url(
            f'function={function}', 
            f'from_currency={from_currency}', 
            f'to_currency={to_currency}'
            )
        data = self._get_response(
            url= url,
            key= 'Realtime Currency Exchange Rate'
            )
        return data
    
    def get_intraday_ex(self, from_symbol, to_symbol, interval):
        function= 'FX_INTRADAY'
        url = self._get_url(
            f'function={function}', 
            f'from_symbol={from_symbol}', 
            f'to_symbol={to_symbol}',
            f'interval={interval}'
            )
        data = self._get_response(
            url= url, 
            key= f'Time Series FX ({interval})'
            )
        'Time Series FX (5min)'
        return data
    
    def get_daily_ex(self, from_symbol, to_symbol):
        function= 'FX_DAILY'
        url = self._get_url(
            f'function={function}', 
            f'from_symbol={from_symbol}', 
            f'to_symbol={to_symbol}'
            )
        data = self._get_response(
            url= url,
            key= 'Time Series FX (Daily)')
        return data
    
    def get_weekly_ex(self, from_symbol, to_symbol):
        function= 'FX_WEEKLY'
        url = self._get_url(
            f'function={function}', 
            f'from_symbol={from_symbol}', 
            f'to_symbol={to_symbol}'
            )
        data = self._get_response(
            url= url,
            key= 'Time Series FX (Weekly)')
        return data
    
    def get_monthly_ex(self, from_symbol, to_symbol):
        function= 'FX_MONTHLY'
        url = self._get_url(
            f'function={function}', 
            f'from_symbol={from_symbol}', 
            f'to_symbol={to_symbol}'
            )
        data = self._get_response(
            url= url,
            key= 'Time Series FX (Monthly)')
        return data



