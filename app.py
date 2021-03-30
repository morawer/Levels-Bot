from datetime import datetime
import time
import requests
import json
import pandas as pd

x = 0

envio = True
envio2 = True

while x == 0:

    excel = "Levels.xlsx"
    df_excel = pd.read_excel(excel)
    values = df_excel["Value"].values
    types = df_excel["Type"].values

    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S >>")
    coin = "btc"
    urlBase = "https://fapi.binance.com/fapi/v1/premiumIndex?symbol=" + coin + "usdt"
    response = requests.get(urlBase).text
    value = json.loads(response)
    price = float(value['markPrice'])

    envio = True
    envio2 = True

    for i in range(len(values)):

        valueFloat = float(values[i])

        rango = 250

        if price < valueFloat - rango and price > valueFloat - rango*2 and envio == True:
            print(date, coin.upper(), f": ${price:.0f} se esta acercando a resistencia de: ",
                  types[i], f" >>>>> {valueFloat:.0f}")
            envio = False
            envio2 = True

        if price < valueFloat and price > valueFloat - rango and envio2 == True:
            print(date, coin.upper(), f": ${price:.0f} esta muy cerca de resistencia de: ",
                  types[i], f" >>>>> {valueFloat:.0f}")
            envio = True
            envio2 = False

        if price > valueFloat + rango and price < valueFloat + rango*2 and envio == True:
            print(date, coin.upper(), f": ${price:.0f} se esta acercando a soporte de: ",
                  types[i], f" >>>>> {valueFloat:.0f}")
            envio = False
            envio2 = True

        if price > valueFloat and price < valueFloat + rango and envio2 == True:
            print(date, coin.upper(), f": ${price:.0f} esta muy cerca de soporte de: ",
                  types[i], f" >>>>> {valueFloat:.0f}")
            envio = True
            envio2 = False

        if price > valueFloat + rango and price < valueFloat + rango:
            envio = True

    time.sleep(10)

    x = 0
