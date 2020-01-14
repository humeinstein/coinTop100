#!/usr/bin/python3
""" print top 100 ACTIVE coins available on coin paprika"""
from coinpaprika import client as Coinpaprika


content = Coinpaprika.Client()
tophund = 0
for coin in content.coins():
    coincopycandle = coin
    coincopytoday = coin
    if coin["is_active"] is True:
        if tophund <= 99:
            print("============================")
            print("Rank: {}\nName: {}\nSymbol: {}\n".format(coin['rank'],coin["name"], coin["symbol"]))
        tophund += 1
    for coin3 in content.today(coincopytoday["id"]):
        print("Today's Session:\nPrice High: {}\nPrice Low: {}\nVolume: {}\n".format(coin3["high"], coin3["low"], coin3["volume"]))


    for coin2 in content.candle(coincopycandle["id"]):
        if tophund <= 99:
            print("Yesterday's Session:\nPrice Open: {}\nPrice Close: {}\nPrice High: {}\nPrice Low: {}\n".format(coin2["open"],coin2["close"], coin2["high"], coin2["low"]))
