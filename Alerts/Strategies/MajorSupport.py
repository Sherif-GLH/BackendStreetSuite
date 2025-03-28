from Alerts.models import Alert
from ..consumers import WebSocketConsumer
from datetime import datetime, timedelta
import requests
from django.conf import settings

def GetMajorSupport(ticker, timespan):
    api_key = settings.FMP_API_KEY
    ## check the limitation number of days accourding to timespan ##
    if timespan == '1day' or timespan == '4hour':
        limit_number_days = 30
    elif timespan == '1hour':
        limit_number_days = 7

    ## get the limitation date ##
    limit_date  = datetime.today() - timedelta(days=limit_number_days)
    counter = 0 ## number of candies that has the same range value 
    largest_number= 0
    smallest_number= 1000000000000000000
    data = requests.get(f'https://financialmodelingprep.com/api/v3/technical_indicator/{timespan}/{ticker.symbol}?type=rsi&period=14&apikey={api_key}')
    results = data.json()
    if results != []:
        try:
            for result in results[1:]:
                ## convert string date to date type ##
                date_of_result = datetime.strptime(result['date'] , "%Y-%m-%d %H:%M:%S")
                if date_of_result >= limit_date:
                    ## check condition of strategy (range of price and date) ## 
                    if (
                        ((abs(results[0]['open']-result['open']) <= 0.8) or 
                        (abs(results[0]['open']-result['close']) <= 0.8) or 
                        (abs(results[0]['close']-result['open']) <= 0.8) or 
                        (abs(results[0]['close']-result['open']) <= 0.8))

                    ):
                        counter += 1
                        largest_number = max(results[0]['open'],results[0]['close'],result['open'],result['close'] , largest_number)
                        smallest_number = min(results[0]['open'],results[0]['close'],result['open'],result['close'] , smallest_number)
                    if counter >= 5:
                        range_of_price = (largest_number+smallest_number)/2
                        alert = Alert.objects.create(ticker=ticker,strategy='Major Support',time_frame=timespan,result_value=range_of_price , Estimated_Revenue=counter)
                        alert.save()
                        WebSocketConsumer.send_new_alert(alert)
                        return alert
        except Exception as e:
            print({"Error" : e })
            return None
        