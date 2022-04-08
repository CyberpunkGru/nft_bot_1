def read_list():
    f = open(f"wallets.txt", "r")
    lines = f.readlines()
    f.close()
    lst = []
    for line in lines:
        if len(line) > 0:
            data = line.split(' ',maxsplit=1)
            address = data[0]
            name = data[1]
            #print(address,name)
            content = address,name
            lst.append(content)
    return lst

def parse_a_transaction(trans):
    hash = trans['hash']
    from_ad = trans['from']
    to_ad= trans['to']
    timstamp = trans['timeStamp']
    contract = trans['contractAddress']#trans['value']
    return hash,from_ad,to_ad,contract,timstamp
