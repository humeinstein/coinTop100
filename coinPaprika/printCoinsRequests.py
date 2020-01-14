#!/usr/bin/python3
""" print coins using requests """
import requests
import sys

if __name__ == '__main__':

    json = requests.get("https://api.coinpaprika.com/v1/coins").json()
    print (json)
