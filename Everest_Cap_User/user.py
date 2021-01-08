class User:
    def __init__(self,user_name, user_ID, ):

    pass

data = 
"""
{'Meta Data': 
{'1. Information': 'Intraday (5min) open, high, low, close prices and volume', 
'2. Symbol': 'AAPL', 
'3. Last Refreshed': '2020-11-16 20:00:00', 
'4. Interval': '5min', 
'5. Output Size': 'Compact', 
'6. Time Zone': 'US/Eastern'}
, 
'Time Series (5min)': 
{'2020-11-16 20:00:00': {'1. open': '119.9400', '2. high': '119.9500', '3. low': '119.8300', '4. close': '119.9000', '5. volume': '19135'}, 
'2020-11-16 19:55:00': {'1. open': '119.9400', '2. high': '119.9500', '3. low': '119.9200', '4. close': '119.9400', '5. volume': '9233'}, 
'2020-11-16 19:50:00': {'1. open': '119.8300', '2. high': '119.9400', '3. low': '119.8300', '4. close': '119.9399', '5. volume': '18264'}, 
'2020-11-16 19:45:00': {'1. open': '119.8200', '2. high': '119.8600', '3. low': '119.8200', '4. close': '119.8300', '5. volume': '12450'}, 
'2020-11-16 19:40:00': {'1. open': '119.8200', '2. high': '119.8400', '3. low': '119.8000', '4. close': '119.8000', '5. volume': '13400'}, 
'2020-11-16 19:35:00': {'1. open': '119.7800', '2. high': '119.8300', '3. low': '119.7500', '4. close': '119.8000', '5. volume': '22307'}, 
'2020-11-16 19:30:00': {'1. open': '119.8800', '2. high': '119.9100', '3. low': '119.7600', '4. close': '119.7700', '5. volume': '25285'}, 
'2020-11-16 19:25:00': {'1. open': '119.9600', '2. high': '119.9600', '3. low': '119.8800', '4. close': '119.9200', '5. volume': '6568'}, 
'2020-11-16 19:20:00': {'1. open': '119.9900', '2. high': '119.9900', '3. low': '119.9300', '4. close': '119.9700', '5. volume': '6114'}, 
'2020-11-16 19:15:00': {'1. open': '119.9700', '2. high': '120.0200', '3. low': '119.9600', '4. close': '120.0000', '5. volume': '11191'}, 
'2020-11-16 19:10:00': {'1. open': '119.9100', '2. high': '119.9700', '3. low': '119.9000', '4. close': '119.9600', '5. volume': '4550'}, 
'2020-11-16 19:05:00': {'1. open': '119.9300', '2. high': '119.9700', '3. low': '119.8900', '4. close': '119.9500', '5. volume': '13354'}, 
'2020-11-16 19:00:00': {'1. open': '119.9800', '2. high': '120.0000', '3. low': '119.9200', '4. close': '119.9300', '5. volume': '12453'}, 
'2020-11-16 18:55:00': {'1. open': '120.0000', '2. high': '120.0200', '3. low': '119.9800', '4. close': '120.0000', '5. volume': '9129'}, 
'2020-11-16 18:50:00': {'1. open': '120.0000', '2. high': '120.0500', '3. low': '119.9800', '4. close': '119.9900', '5. volume': '5933'}, 
'2020-11-16 18:45:00': {'1. open': '120.0800', '2. high': '120.0800', '3. low': '120.0000', '4. close': '120.0000', '5. volume': '8587'}, 
'2020-11-16 18:40:00': {'1. open': '120.0100', '2. high': '120.1000', '3. low': '120.0100', '4. close': '120.0600', '5. volume': '7961'}, 
'2020-11-16 18:35:00': {'1. open': '120.0500', '2. high': '120.0500', '3. low': '119.9800', '4. close': '120.0500', '5. volume': '12815'},
 '2020-11-16 18:30:00': {'1. open': '120.0100', '2. high': '120.0500', '3. low': '120.0100', '4. close': '120.0100', '5. volume': '8542'}, 
 '2020-11-16 18:25:00': {'1. open': '120.0200', '2. high': '120.0300', '3. low': '120.0100', '4. close': '120.0100', '5. volume': '14602'}, 
 '2020-11-16 18:20:00': {'1. open': '120.0300', '2. high': '120.0600', '3. low': '120.0000', '4. close': '120.0300', '5. volume': '16814'}, 
 '2020-11-16 18:15:00': {'1. open': '120.0300', '2. high': '120.0800', '3. low': '120.0100', '4. close': '120.0300', '5. volume': '25314'}, '2020-11-16 18:10:00': {'1. open': '120.0500', '2. high': '120.0700', '3. low': '120.0100', '4. close': '120.0500', '5. volume': '10384'}, '2020-11-16 18:05:00': {'1. open': '120.0600', '2. high': '120.3200', '3. low': '120.0500', '4. close': '120.0500', '5. volume': '19498'}, '2020-11-16 18:00:00': {'1. open': '120.0100', '2. high': '120.0600', '3. low': '120.0100', '4. close': '120.0600', '5. volume': '10830'}, '2020-11-16 17:55:00': {'1. open': '120.0700', '2. high': '120.0700', '3. low': '120.0100', '4. close': '120.0100', '5. volume': '17856'}, '2020-11-16 17:50:00': {'1. open': '120.0200', '2. high': '120.1400', '3. low': '119.9500', '4. close': '120.0600', '5. volume': '25020'}, '2020-11-16 17:45:00': {'1. open': '120.1300', '2. high': '120.1300', '3. low': '120.0000', '4. close': '120.0100', '5. volume': '18242'}, '2020-11-16 17:40:00': {'1. open': '120.0500', '2. high': '120.1300', '3. low': '120.0400', '4. close': '120.1100', '5. volume': '14458'}, '2020-11-16 17:35:00': {'1. open': '120.1800', '2. high': '120.1800', '3. low': '120.0100', '4. close': '120.1200', '5. volume': '24460'}, '2020-11-16 17:30:00': {'1. open': '120.2200', '2. high': '120.2300', '3. low': '120.1001', '4. close': '120.1500', '5. volume': '22898'}, '2020-11-16 17:25:00': {'1. open': '120.2700', '2. high': '120.3000', '3. low': '120.1800', '4. close': '120.1800', '5. volume': '50245'}, '2020-11-16 17:20:00': {'1. open': '120.3300', '2. high': '120.4300', '3. low': '120.2400', '4. close': '120.2700', '5. volume': '17303'}, '2020-11-16 17:15:00': {'1. open': '120.3300', '2. high': '120.3600', '3. low': '120.3300', '4. close': '120.3400', '5. volume': '5394'}, 
 '2020-11-16 17:10:00': {'1. open': '120.3500', '2. high': '120.3700', '3. low': '120.3300', '4. close': '120.3600', '5. volume': '69012'}, '2020-11-16 17:05:00': {'1. open': '120.4002', '2. high': '120.4100', '3. low': '120.3500', '4. close': '120.3500', '5. volume': '10152'}, '2020-11-16 17:00:00': {'1. open': '120.4200', '2. high': '120.4200', '3. low': '120.3500', '4. close': '120.4000', '5. volume': '14333'}, '2020-11-16 16:55:00': {'1. open': '120.3700', '2. high': '120.4700', '3. low': '120.3500', '4. close': '120.4200', '5. volume': '13279'}, '2020-11-16 16:50:00': {'1. open': '120.3100', '2. high': '120.3900', '3. low': '120.3000', '4. close': '120.3600', '5. volume': '527464'}, '2020-11-16 16:45:00': {'1. open': '120.3002', '2. high': '120.3600', '3. low': '120.3000', '4. close': '120.3100', '5. volume': '15878'}, '2020-11-16 16:40:00': {'1. open': '120.2000', '2. high': '120.3000', '3. low': '120.2000', '4. close': '120.3000', '5. volume': '12883'}, '2020-11-16 16:35:00': {'1. open': '120.3500', '2. high': '120.3500', '3. low': '120.1800', '4. close': '120.2000', '5. volume': '18632'}, '2020-11-16 16:30:00': {'1. open': '120.3000', '2. high': '120.3500', '3. low': '120.3000', '4. close': '120.3500', '5. volume': '26720'}, '2020-11-16 16:25:00': {'1. open': '120.2898', '2. high': '120.3000', '3. low': '120.2100', '4. close': '120.3000', '5. volume': '24110'}, '2020-11-16 16:20:00': {'1. open': '120.3600', '2. high': '120.3600', '3. low': '120.2200', '4. close': '120.2800', '5. volume': '18758'}, '2020-11-16 16:15:00': {'1. open': '120.2800', '2. high': '120.3500', '3. low': '120.2500', '4. close': '120.3500', '5. volume': '154635'}, '2020-11-16 16:10:00': {'1. open': '120.2726', '2. high': '120.3000', '3. low': '120.1700', '4. close': '120.2700', '5. volume': '60580'}, '2020-11-16 16:05:00': {'1. open': '120.4700', '2. high': '120.4700', '3. low': '120.0900', '4. close': '120.3000', '5. volume': '2984199'}, '2020-11-16 16:00:00': {'1. open': '119.9300', '2. high': '120.5000', '3. low': '119.8300', '4. close': '120.3500', '5. volume': '4610966'}, '2020-11-16 15:55:00': {'1. open': '119.9500', '2. high': '119.9800', '3. low': '119.7300', '4. close': '119.9150', '5. volume': '1269598'}, '2020-11-16 15:50:00': {'1. open': '120.0250', '2. high': '120.1000', '3. low': '119.9500', '4. close': '119.9500', '5. volume': '827319'}, '2020-11-16 15:45:00': {'1. open': '119.9550', '2. high': '120.0800', '3. low': '119.9213', '4. close': '120.0232', '5. volume': '776157'}, '2020-11-16 15:40:00': {'1. open': '120.0000', '2. high': '120.0700', '3. low': '119.9100', '4. close': '119.9600', '5. volume': '665893'}, '2020-11-16 15:35:00': {'1. open': '119.9241', '2. high': '120.0500', '3. low': '119.8516', '4. close': '120.0000', '5. volume': '732508'}, '2020-11-16 15:30:00': {'1. open': '119.9850', '2. high': '120.0700', '3. low': '119.7800', '4. close': '119.9258', '5. volume': '843895'}, '2020-11-16 15:25:00': {'1. open': '119.8750', '2. high': '120.1300', '3. low': '119.8300', '4. close': '119.9850', '5. volume': '980234'}, '2020-11-16 15:20:00': {'1. open': '119.7000', '2. high': '120.2048', '3. low': '119.6700', '4. close': '119.8701', '5. volume': '671238'}, '2020-11-16 15:15:00': {'1. open': '119.7850', '2. high': '120.7900', '3. low': '119.7000', '4. close': '119.7000', '5. volume': '778220'}, '2020-11-16 15:10:00': {'1. open': '119.6500', '2. high': '119.8093', '3. low': '119.6448', '4. close': '119.7821', '5. volume': '809666'}, '2020-11-16 15:05:00': {'1. open': '119.9075', '2. high': '120.0000', '3. low': '119.6400', '4. close': '119.6450', '5. volume': '1200500'}, '2020-11-16 15:00:00': {'1. open': '119.8684', '2. high': '119.9500', '3. low': '119.8600', '4. close': '119.9050', '5. volume': '439297'}, '2020-11-16 14:55:00': {'1. open': '119.9150', '2. high': '119.9932', '3. low': '119.7900', '4. close': '119.8693', '5. volume': '733073'}, '2020-11-16 14:50:00': {'1. open': '119.9400', '2. high': '120.0600', '3. low': '119.8191', '4. close': '119.9200', '5. volume': '753594'}, '2020-11-16 14:45:00': {'1. open': '120.0584', '2. high': '120.0584', '3. low': '119.9050', '4. close': '119.9445', '5. volume': '797975'}, '2020-11-16 14:40:00': {'1. open': '120.0800', '2. high': '120.1450', '3. low': '119.9400', '4. close': '120.0550', '5. volume': '962536'}, '2020-11-16 14:35:00': {'1. open': '120.3118', '2. high': '120.3200', '3. low': '120.0700', '4. close': '120.0800', '5. volume': '681391'}, '2020-11-16 14:30:00': {'1. open': '120.3610', '2. high': '120.3700', '3. low': '120.2700', '4. close': '120.3100', '5. volume': '538904'}, '2020-11-16 14:25:00': {'1. open': '120.1750', '2. high': '120.3650', '3. low': '120.1400', '4. close': '120.3603', '5. volume': '613071'}, '2020-11-16 14:20:00': {'1. open': '120.2150', '2. high': '120.2184', '3. low': '120.1101', '4. close': '120.1750', '5. volume': '416758'}, '2020-11-16 14:15:00': {'1. open': '120.1243', '2. high': '120.2200', '3. low': '120.0400', '4. close': '120.2144', '5. volume': '526679'}, '2020-11-16 14:10:00': {'1. open': '120.1300', '2. high': '120.1800', '3. low': '120.0200', '4. close': '120.1250', '5. volume': '471577'}, '2020-11-16 14:05:00': {'1. open': '120.2200', '2. high': '120.2500', '3. low': '120.0514', '4. close': '120.1400', '5. volume': '545583'}, '2020-11-16 14:00:00': {'1. open': '120.1500', '2. high': '120.2800', '3. low': '120.0900', '4. close': '120.2200', '5. volume': '608323'}, '2020-11-16 13:55:00': {'1. open': '120.0700', '2. high': '120.1700', '3. low': '120.0300', '4. close': '120.1450', '5. volume': '429617'}, '2020-11-16 13:50:00': {'1. open': '120.1300', '2. high': '120.2000', '3. low': '120.0200', '4. close': '120.0600', '5. volume': '744404'}, '2020-11-16 13:45:00': {'1. open': '120.3337', '2. high': '120.3500', '3. low': '120.0000', '4. close': '120.1339', '5. volume': '1139286'}, '2020-11-16 13:40:00': {'1. open': '120.3700', '2. high': '120.4300', '3. low': '120.2908', '4. close': '120.3400', '5. volume': '546925'}, '2020-11-16 13:35:00': {'1. open': '120.1750', '2. high': '120.3800', '3. low': '120.1600', '4. close': '120.3700', '5. volume': '630989'}, '2020-11-16 13:30:00': {'1. open': '120.3800', '2. high': '120.3800', '3. low': '120.1500', '4. close': '120.1800', '5. volume': '653100'}, '2020-11-16 13:25:00': {'1. open': '120.5600', '2. high': '120.5900', '3. low': '120.2400', '4. close': '120.3800', '5. volume': '670937'}, '2020-11-16 13:20:00': {'1. open': '120.4400', '2. high': '120.5800', '3. low': '120.3700', '4. close': '120.5500', '5. volume': '493345'}, '2020-11-16 13:15:00': {'1. open': '120.5050', '2. high': '120.5900', '3. low': '120.4000', '4. close': '120.4350', '5. volume': '557765'}, '2020-11-16 13:10:00': {'1. open': '120.2800', '2. high': '120.5700', '3. low': '120.2600', '4. close': '120.5001', '5. volume': '686159'}, '2020-11-16 13:05:00': {'1. open': '120.4250', '2. high': '120.4500', '3. low': '120.1600', '4. close': '120.2750', '5. volume': '899419'}, '2020-11-16 13:00:00': {'1. open': '120.3799', '2. high': '120.4700', '3. low': '120.2800', '4. close': '120.4300', '5. volume': '842820'}, '2020-11-16 12:55:00': {'1. open': '120.6400', '2. high': '120.6800', '3. low': '120.3500', '4. close': '120.3750', '5. volume': '716867'}, '2020-11-16 12:50:00': {'1. open': '120.8201', '2. high': '120.8207', '3. low': '120.5700', '4. close': '120.6350', '5. volume': '572205'}, '2020-11-16 12:45:00': {'1. open': '120.6400', '2. high': '120.8300', '3. low': '120.6300', '4. close': '120.8202', '5. volume': '641979'}, '2020-11-16 12:40:00': {'1. open': '120.5850', '2. high': '120.6700', '3. low': '120.5400', '4. close': '120.6406', '5. volume': '399000'}, '2020-11-16 12:35:00': {'1. open': '120.6450', '2. high': '120.6500', '3. low': '120.5200', '4. close': '120.5800', '5. volume': '477575'}, '2020-11-16 12:30:00': {'1. open': '120.5300', '2. high': '120.6750', '3. low': '120.5250', '4. close': '120.6500', '5. volume': '550390'}, '2020-11-16 12:25:00': {'1. open': '120.7100', '2. high': '120.7199', '3. low': '120.4400', '4. close': '120.5350', '5. volume': '820089'}, '2020-11-16 12:20:00': {'1. open': '120.7900', '2. high': '120.8200', '3. low': '120.6300', '4. close': '120.7100', '5. volume': '641890'}, '2020-11-16 12:15:00': {'1. open': '120.8250', '2. high': '120.8899', '3. low': '120.7600', '4. close': '120.8000', '5. volume': '638474'}, '2020-11-16 12:10:00': {'1. open': '120.8300', '2. high': '120.9900', '3. low': '120.7800', '4. close': '120.8257', '5. volume': '1123179'}, '2020-11-16 12:05:00': {'1. open': '120.7450', '2. high': '120.9300', '3. low': '120.7300', '4. close': '120.8300', '5. volume': '964403'}, '2020-11-16 12:00:00': {'1. open': '120.7700', '2. high': '120.8000', '3. low': '120.6400', '4. close': '120.7450', '5. volume': '700126'}, '2020-11-16 11:55:00': {'1. open': '120.5100', '2. high': '120.7900', '3. low': '120.4800', '4. close': '120.7800', '5. volume': '817398'}, '2020-11-16 11:50:00': {'1. open': '120.4700', '2. high': '120.5682', '3. low': '120.3800', '4. close': '120.5100', '5. volume': '586317'}, '2020-11-16 11:45:00': {'1. open': '120.5100', '2. high': '120.5300', '3. low': '120.4050', '4. close': '120.4800', '5. volume': '544463'}}}
 """ 