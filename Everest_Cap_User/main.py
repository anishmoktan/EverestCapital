from alphavantage import search_stock
import requests

data = requests.get('https://ipinfo.io/json')
data = data.json()
print(data['city'])
print(data['region'])


search_stock('TSLA')

#Can be used to record ip addresses of the users who sign up