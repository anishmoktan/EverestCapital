import json
import requests
import os

class search_stock:
  def __init__(self, stock_symbol):
      stock_symbol = stock_symbol.upper()
      base_url  = "https://www.alphavantage.co/query?"
      key = 1
      query_params = {"function": "TIME_SERIES_INTRADAY" , "symbol": stock_symbol, "interval": "5min", "apikey": key}
      try:
          response = requests.get(base_url, query_params)
          data = response.json()
          if response.status_code == 200:
              last_referesh = data['Meta Data']["3. Last Refreshed"]
              self.value= float(data["Time Series (5min)"][last_referesh]["1. open"])
              print("The market price for" + " " + stock_symbol + " "+ "stock is currently $" + str(self.value) + "\n")
          elif response.status_code == 404:
              print("404 error")
      except KeyError:
          print(stock_symbol + " does not exist")
    
    #   if response.status_code == 200:
    #       print('\nWe were able to find the value of the stock!')
    #   elif response.status_code == 404:
    #       print('Sorry we could not find the stock you were looking for')
    #       return(self.search_stock)

    
      
      
  