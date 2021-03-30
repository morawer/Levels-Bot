import time
import requests
import json
import pandas as pd

x = 0

while x == 0:

    excel = "Levels.xlsx"
    df_excel = pd.read_excel(excel)
    values = df_excel["Value"].values
    types = df_excel["Type"].values

    coin = "btc"
    urlBase = "https://fapi.binance.com/fapi/v1/premiumIndex?symbol=" + coin + "usdt"
    response = requests.get(urlBase).text
    value = json.loads(response)
    price = float(value['markPrice'])

    for i in range(len(values)):

        valueFloat = float(values[i])

        if price < valueFloat - 500 and price > valueFloat - 1000:
            print("El precio es de ", price, "se esta acercando a resistencia de: ",
                  types[i], " >>>>> ", valueFloat)

        if price < valueFloat and price > valueFloat - 500:
            print("El precio es de ", price, "esta muy cerca de resistencia de: ",
                  types[i], " >>>>> ", valueFloat)

        if price > valueFloat + 500 and price < valueFloat + 1000:
            print("El precio es de ", price, "se esta acercando a soporte de: ",
                  types[i], " >>>>> ", valueFloat)

        if price > valueFloat and price < valueFloat + 500:
            print("El precio es de ", price, "esta muy cerca de soporte de: ",
                  types[i], " >>>>> ", valueFloat)

    time.sleep(30)

    x = 0

