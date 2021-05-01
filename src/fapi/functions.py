from websocket import create_connection
from env.test import fapi, endpoint
import json

def login():
    ws = create_connection(endpoint)
    ws.send(json.dumps({
        	"command": "login",
        	"arguments": fapi
    }))

    login = ws.recv()
    print(login)

    return ws

def getSymbol(ws, symbol):
        ws.send(json.dumps({
        	"command": "getSymbol",
        	"arguments": {
        		"symbol": symbol
        	}
        }))

        data = ws.recv()

        return data
