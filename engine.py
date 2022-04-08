from wallet_parser import *
from ethAPI import *
from webhook import sendWebhook
fetched = {}


def init():
    global fetched
    wallets = read_list()
    for i in wallets:
        try:
            address , name = i 
            lst = get_Transactions(address)
            for i in lst : 
                try:
                    hash,from_ad,to_ad,contract,tim = parse_a_transaction(i)
                   # price = int(price)/1000000000000000000
                    if address not in fetched.keys():
                        fetched[address] = []
                    fetched[address].append(hash)
                except:
                    print("Error in parsing a transaction of wallet",address)
        except:
            print("Error in getting transactions for a wallet")
        
def run():
    wallets = read_list()
    global fetched
    for i in wallets:
        try:
            address , name = i 
            lst = get_Transactions(address)
            for i in reversed(lst) : 
                try:
                    hash,from_ad,to_ad,contract,tim = parse_a_transaction(i)
                    #print(hash,from_ad,to_ad,contract,tim)
                    if hash in fetched[address]:
                        continue
                    fetched[address].append(hash)
                    if len(fetched[address]) > 30:
                        fetched[address] = fetched[address][10:]
                        print("clear")
                    typee = 'OUT'
                    #print(to_ad,address)
                    if int(from_ad,16) == int(to_ad,16):
                        typee = 'SELF'

                    if int(to_ad,16) == int(address,16):
                        typee = 'IN'
                 
                    try:
                        sendWebhook(hash,from_ad,to_ad,contract,typee,address,name,tim)
                        
                    except:
                        print("Error in sending webhook")
                    time.sleep(1)
                except:
                    print("Error in parsing a transaction of wallet",address)
        except:
            print("Error in getting transactions for a wallet")
#init()
#run()

