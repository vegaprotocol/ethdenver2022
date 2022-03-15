#!/usr/bin/python3

import json
import os
import requests
import time


# Specify your target Vega market identifier for LP
marketID = "0f9010dd89786e39e9fbc5a01ab5fd1559b5b24109ad5e9a8ccb92618271e7ea"


#####################################################################################
#                             W A L L E T   S E R V I C E                           #
#####################################################################################

node_url_rest = os.getenv("NODE_URL_REST")
wallet_server_url = os.getenv("WALLETSERVER_URL")
wallet_name = os.getenv("WALLET_NAME")
wallet_passphrase = os.getenv("WALLET_PASSPHRASE")

print(f"Logging into wallet: {wallet_name}")

# Log in to an existing wallet
req = {"wallet": wallet_name, "passphrase": wallet_passphrase}
response = requests.post(f"{wallet_server_url}/api/v1/auth/token", json=req)
token = response.json()["token"]

assert token != ""
print("Logged in to wallet successfully")

# List key pairs and select public key to use
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{wallet_server_url}/api/v1/keys", headers=headers)
keys = response.json()["keys"]
pubkey = keys[0]["pub"]

assert pubkey != ""
print(f"Selected pubkey: {pubkey}")


#####################################################################################
#                  N E W  L I Q U I D I T Y   C O M M I T M E N T                   #
#####################################################################################

# Request liquidity provisions for the market
url = "{base}/liquidity-provisions/party/{party}/market/{marketId}".format(base=node_url_rest, party=pubkey, marketId=marketID)
response = requests.get(url)
response_json = response.json()

print("Liquidity provisions:\n{}".format(json.dumps(response_json, indent=2, sort_keys=True)))
