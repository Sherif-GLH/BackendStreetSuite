from Alerts.models import Alert
import requests, time
from ..consumers import WebSocketConsumer

def GetUnusualOptionBuys(ticker): 
    token = 'a4c1971d-fbd2-417e-a62d-9b990309a3ce'  
    ## for Authentication on request ##
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'  # Optional, depending on the API requirements
    }
    ticker_count = 0
    ## looping on tickers ##
    ticker_count += 1
    print(f"unusiual options {ticker_count}")
    if ticker_count % 119 == 0:
        time.sleep(40)
    response = requests.get(
        f'https://api.unusualwhales.com/api/stock/{ticker.symbol}/options-volume', headers=headers).json()    
    try:
        ## to get avg of call transaction ##
        avg_30_day_call_volume = response['data'][0]['avg_30_day_call_volume']
        ## average number of put transaction ##
        avg_30_day_put_volume = response['data'][0]['avg_30_day_put_volume']
        ### get all contracts for each ticker ###    
        contract_options = requests.get(f'https://api.unusualwhales.com/api/stock/{ticker.symbol}/option-contracts',headers=headers).json()['data']
        ## looping on each contract ##
        for contract in contract_options:
            volume = contract['volume']
            contract_id = contract['option_symbol']
            if contract_id[-9] == 'C':
                if float(volume) > float(avg_30_day_call_volume):
                    alert = Alert.objects.create(ticker=ticker 
                        ,strategy='Unusual Option Buys' ,time_frame='1day' ,result_value=volume, 
                        risk_level= 'Call' ,investor_name=contract_id , amount_of_investment= avg_30_day_call_volume)
                    alert.save()
                    WebSocketConsumer.send_new_alert(alert)
            else:
                if float(volume) > float(avg_30_day_put_volume):
                        alert = Alert.objects.create(ticker=ticker 
                            ,strategy='Unusual Option Buys' ,time_frame='1day' ,result_value=volume, 
                            risk_level= 'Put' ,investor_name=contract_id , amount_of_investment= avg_30_day_put_volume)
                        alert.save()
                        WebSocketConsumer.send_new_alert(alert)
    except Exception as e:
        print({'error' : e})