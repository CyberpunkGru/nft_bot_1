import requests
from datetime import datetime
def sendWebhook(hash,from_ad,to_ad,contract,typee,address,name,timestamp='1545730073'):
    url = 'https://discord.com/api/webhooks/885812100834938970/oy9hlU2o12mQBXJDbclp-eoKStVf5MBiKZTBMb-v4mFT24kJa9ofNyWv3FxGDqD_4w9s'
    data = {}
    dt_object = datetime.fromtimestamp(int(timestamp))
    hash_url = f'https://etherscan.io/tx/{hash}'
    from_url = f'https://etherscan.io/address/{from_ad}'
    to_url = f'https://etherscan.io/address/{to_ad}'
    add_url = f'https://etherscan.io/address/{address}'
    contract_url =f'https://etherscan.io/address/{contract}'
    type_field = {
        'name' : 'Type',
        'value' : typee,
        'inline' : True
    }
    from_field = {
        'name' : 'From',
        'value' : f'[{from_ad}]({from_url})',
        'inline' : True
    }
    to_field = {
        'name' : 'To',
        'value' : f'[{to_ad}]({to_url})',
        'inline' : True
    }
    add_field = {
        'name' : 'Name',
        'value' : f'[{name}]({add_url})',
        'inline' : True
    }
    contract_field = {
        'name' : 'Contract Address',
        'value' : f'[{contract}]({contract_url})',
        'inline' : True
    }
    hash_field = {
        'name' : 'Hash_URL',
        'value' : f'[Tx_Hash]({hash_url})',
        'inline' : True
    }
    data["embeds"] = [
        {
            #"description" : "text in embed",
            "title" : 'Transaction Details',
            'timestamp' : str(dt_object),
            "url" : hash_url,
            'fields' : [
                add_field,
                contract_field,
                type_field,
                from_field,
                to_field,
                hash_field
                
            ]
        }
    ]
    result = requests.post(url , json= data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

