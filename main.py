from websocket import create_connection
from src.fapi.functions import login, getSymbol
import json
import time

ws = login()

while True:

    symbol = getSymbol(ws, "EURUSD")

    print(symbol)

    time.sleep(3)
