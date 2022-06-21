import http.client
import json
from datetime import datetime

#TODO transform into class!
f = open("key.txt", "r")
key = f.read()

def readSymbol(name) -> None:
    conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    query = "/auto-complete?q=" + name + "&region=US"

    conn.request("GET", query, headers=headers)

def read(sign, interval, range) -> None:
    conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    #interval: (5m | 15m | 1d | 1wk | 1mo)
    #range:  (1d | 5d | 3mo | 6mo | 1y | 5y | max)
    query = "/market/get-charts?symbol=" + sign + "&interval=" + interval +"&range="+ range +"&region=US"

    conn.request("GET", query, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def getValue(obj) -> None:
    jObj = json.loads(obj)
    
    a_info = list()
    a_time = list()
    a_value = list()

    info = jObj["chart"]["result"][0]["meta"]
    timestamps = jObj["chart"]["result"][0]["timestamp"]
    chartValue = jObj["chart"]["result"][0]["indicators"]["quote"][0]["close"] 

    a_info.append(info["symbol"])
    a_info.append(info["currency"])

    for x in range(0, len(timestamps)):
        time = datetime.fromtimestamp(timestamps[x])
        a_time.append(time)
        value = chartValue[x]
        a_value.append(value)

    return [a_time, a_value, a_info]

def printValue(obj) -> None:
    
    print('Name of Stock: ' + obj[2][0])
    print('Currency of Stock: ' + obj[2][1])
    
    for x in range(0, len(obj[0])):
        print(str(obj[0][x]) + " | Value : " + str(round(obj[1][x], 2)))
