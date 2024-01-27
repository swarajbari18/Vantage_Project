import requests
import pandas as pd
from Forex_endpoint.settings import API_KEY



class API_INTERFACE:
    '''
    Python class that interacts with the Vantage API
    '''

    def __init__(self, API_KEY= API_KEY) -> None:
        '''
        Constructing variables, 
        API_KEY: This is the key required to authenticate with the API, fetched from the enviroment variable.
        '''
        self.url_head = 'https://www.alphavantage.co/query?'
        self.API_KEY = API_KEY



    def _get_url(self, *args):
        '''
        Takes all the arguments and joins them to form a url to request on
        Each function requires differfrent paraeters so the url changes,
        Therefore this function is neccesary.
        '''
        return self.url_head + '&'.join(args) + f'&apikey={self.API_KEY}'



    def _get_response(self, url, key):
        '''
        Takes the url and reuests data from it.
        If reuest is successful, then it converts the series of json to a readable
        pandas dataframe and converts it to a html table.
        '''
        try:
            r = requests.get(url)
            r.raise_for_status()  # Raise an HTTPError for bad responses
            data = r.json()[key]

            if key == 'Realtime Currency Exchange Rate':
                data = pd.DataFrame([data]).T.to_html()
            else:
                data = pd.DataFrame(data).T.to_html()

            return {'html_table': data}

        except requests.exceptions.RequestException as e:
            return {'error': f"Request failed: {str(e)}"}
        except KeyError as e:
            return {'error': f"Key not found in response: {str(e)}"}
        except Exception as e:
            return {'error': f"An unexpected error occurred: {str(e)}"}
        


    def get_current_ex(self, from_currency, to_currency):
        '''
        This function deals with the CURRENCY_EXCHANGE_RATE function of the API.
        This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD).
        Args:
            from_currency: The currency you would like to get the exchange rate for. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: from_currency=USD or from_currency=BTC.
            to_currency: The destination currency for the exchange rate. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: to_currency=USD or to_currency=BTC

        '''
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
        '''
        This function deals with the FX_INTRADAY function of the API.
        This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD).
        Args:
            from_symbol: The currency you would like to get the exchange rate for. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: from_currency=USD or from_currency=BTC.
            to_symbol: The destination currency for the exchange rate. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: to_currency=USD or to_currency=BTC
            interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min

        '''
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
        '''
        This function deals with the FX_DAILY function of the API.
        This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD).
        Args:
            from_symbol: The currency you would like to get the exchange rate for. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: from_currency=USD or from_currency=BTC.
            to_symbol: The destination currency for the exchange rate. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: to_currency=USD or to_currency=BTC

        '''
        function= 'FX_DAILY'
        url = self._get_url(
            f'function={function}', 
            f'from_symbol={from_symbol}', 
            f'to_symbol={to_symbol}'
            )
        data = self._get_response(
            url= url,
            key= 'Time Series FX (Daily)'
            )
        return data



    def get_weekly_ex(self, from_symbol, to_symbol):
        '''
        This function deals with the FX_WEEKLYfunction of the API.
        This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD).
        Args:
            from_symbol: The currency you would like to get the exchange rate for. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: from_currency=USD or from_currency=BTC.
            to_symbol: The destination currency for the exchange rate. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: to_currency=USD or to_currency=BTC

        '''
        function= 'FX_WEEKLY'
        url = self._get_url(
            f'function={function}', 
            f'from_symbol={from_symbol}', 
            f'to_symbol={to_symbol}'
            )
        data = self._get_response(
            url= url,
            key= 'Time Series FX (Weekly)'
            )
        return data


 
    
    def get_monthly_ex(self, from_symbol, to_symbol):
        '''
        This function deals with the FX_MONTHLY function of the API.
        This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD).
        Args:
            from_symbol: The currency you would like to get the exchange rate for. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: from_currency=USD or from_currency=BTC.
            to_symbol: The destination currency for the exchange rate. 
                            It can either be a physical currency or digital/crypto currency. 
                            For example: to_currency=USD or to_currency=BTC

        '''
        function= 'FX_MONTHLY'
        url = self._get_url(
            f'function={function}', 
            f'from_symbol={from_symbol}', 
            f'to_symbol={to_symbol}'
            )
        data = self._get_response(
            url= url,
            key= 'Time Series FX (Monthly)'
            )
        return data



