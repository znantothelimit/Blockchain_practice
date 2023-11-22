# -*- coding: utf-8 -*-

import requests

# pip install requests

# block_number = 12345
block_number = input("Enter Block Number : ")
print("Block Number is ", block_number)

# Blockchain.com API End Point
api_url = f"https://blockchain.info/rawblock/{block_number}"

try:
    response = requests.get(api_url)

    if response.status_code == 200:
        block_data = response.json()
#       print(f"{block_number}th Block :\n{block_data}")
        print(f"\n{block_number}th Block")
        for key, value in block_data.items():
           print(f'{key}: {value}')
    else:
        print(f"API Request Fail. Error Code = {response.status_code}")

except Exception as e:
    print(f"Error : {e}")
