from os import times
import requests
import json
import time

def get_Transactions(address, api = 'ZUBJ373NSJR9VX4XWGBXKBY6S247DG837M'):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=desc&apikey={api}'
    url2 = f'https://api.etherscan.io/api?module=account&action=tokennfttx&address={address}&page=1&offset=3&sort=desc&apikey={api}'
    r = requests.get(url= url2)

    cnt = 0 
    while r.status_code!=200 : 
        cnt = cnt + 1
        r = requests.get(url= url2)
        time.sleep(cnt *cnt + 1)
        if cnt > 5:
            print("ERRRRRRROR IN ETHERSCAN", r.status_code)
            print("ERRRRRRROR IN ETHERSCAN", r.status_code)
            print("ERRRRRRROR IN ETHERSCAN", r.status_code)
            print("ERRRRRRROR IN ETHERSCAN", r.status_code)
            print("ERRRRRRROR IN ETHERSCAN", r.status_code)
            return []
    jsonn = json.loads(r.text)
    arr = jsonn['result']
    return arr

#print(get_Transactions('0x3889A7996eF845FE35105b3ef8b0182Fd3c253d6'))