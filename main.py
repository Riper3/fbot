from websocket import create_connection
from src.fapi.functions import login, getSymbol
import json
import time
from src.mysql.mysql import select, insert



ws = login()

symbols = select('SELECT symbol_name, symbol_id from symbols WHERE status = 1')

while True:

    for symbol in symbols:
        symboldata = json.loads(getSymbol(ws, symbol['symbol_name']))

        print(symboldata)

        response = symboldata['returnData']

        data = (
        symbol['symbol_id'],
        response['bid'],
        response['ask'],
        )

        insert('INSERT INTO price_history (symbol_id, bid, ask, date) VALUES (%s, %s, %s, CURRENT_TIMESTAMP())', data)
        time.sleep(0.2)

    time.sleep(10)
