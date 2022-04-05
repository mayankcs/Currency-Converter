import requests

def get_exchange_rate(source,target,date=0):
    if date==0:
        url = 'https://api.exchangerate.host/convert?from=%s&to=%s'%(source,target)
    else:    
        url = 'https://api.exchangerate.host/convert?from=%s&to=%s&date=%s'%(source,target,date)

    response = requests.get(url)
    data = response.json()
    return [data['info']['rate'],data['date']]





