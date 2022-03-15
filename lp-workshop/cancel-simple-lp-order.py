#!/usr/bin/python3

import json
import os
import requests


# Specify your target Vega market identifier for LP
marketID = "0f9010dd89786e39e9fbc5a01ab5fd1559b5b24109ad5e9a8ccb92618271e7ea"


#####################################################################################
#                             W A L L E T   S E R V I C E                           #
#####################################################################################

node_url_rest = os.getenv("NODE_URL_REST")
wallet_server_url = os.getenv("WALLETSERVER_URL")
wallet_name = os.getenv("WALLET_NAME")
wallet_passphrase = os.getenv("WALLET_PASSPHRASE")

# Log in to an existing wallet
req = {"wallet": wallet_name, "passphrase": wallet_passphrase}
response = requests.post(f"{wallet_server_url}/api/v1/auth/token", json=req)
token = response.json()["token"]

assert token != ""

# List key pairs and select public key to use
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{wallet_server_url}/api/v1/keys", headers=headers)
keys = response.json()["keys"]
pubkey = keys[0]["pub"]

assert pubkey != ""
print(f"Selected pubkey from wallet: {pubkey}")



#####################################################################################
#               C A N C E L    L I Q U I D I T Y   C O M M I T M E N T              #
#####################################################################################

# Compose a liquidity commitment order message
# (it will now serve as a cancellation request): set commitmentAmount to 0,
# note that transaction may get rejected if removing previously supplied liquidity 
# will result in insufficient liquidity for the market
submission = {
    "liquidityProvisionCancellation": {
        "marketId": marketID,
        "commitmentAmount": "0"
    },
    "pubKey": pubkey,
    "propagate": True
}

print("Liquidity provision cancellation: ", json.dumps(submission, ensure_ascii=True, indent=4))

# Sign the transaction with a liquidity provision submission command
url = f"{wallet_server_url}/api/v1/command/sync"
response = requests.post(url, headers=headers, json=submission)

print("Signed liquidity commitment (cancellation) and sent to Vega")
print(response.json())

# Completed.
