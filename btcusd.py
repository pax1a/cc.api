#bitfinex API
#https://docs.bitfinex.com/v1/reference

from urllib.request import urlopen
import json
from time import sleep
from datetime import datetime

url = "https://api.bitfinex.com/v1/pubticker/btcusd"
data = json.load(urlopen(url))
pre = float(data['mid'])
print(pre)

lmid = [pre]*720 #List of mid

while True:
    try:
        data = json.load(urlopen(url))

        lmin = min(lmid)
        lmax = max(lmid)
        act = float(data['mid'])

        if act > lmax:
            print('Max: ' + str(act) + ' '  + datetime.fromtimestamp(float(data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))

        if act < lmin:
            print('Min: ' + str(act) + ' ' + datetime.fromtimestamp(float(data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))


        #print(data['mid'] + " " + str(round(float(data['mid'])/pre*100-100, 2)) + "% - " + datetime.fromtimestamp(float(data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))

        #pre = float(data['mid'])
        pre = act

        lmid = lmid[1:720]
        lmid.append(pre)

        sleep(5)
    except:
        print("No connection")
        sleep(5)
