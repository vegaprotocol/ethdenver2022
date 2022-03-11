#!/usr/bin/python3

import json
import os
import requests
import time


# Specify your target Vega market identifier for LP
marketID = "3a95f7c59914463942fb1d495e06dce0c13402de3c27d12be576bac629b85c80"


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

# Note: commitmentAmount is an integer. For example 123456 is a price of 1.23456,
# for a market which is configured to have a precision of 5 decimal places.

# Compose your submit liquidity provision command
submission = {
    "liquidityProvisionSubmission": {
        "marketId": marketID,
        "commitmentAmount": "100",
        "fee": "0.01",
        "buys": [
            {
                "offset": "1",
                "proportion": "1",
                "reference": "PEGGED_REFERENCE_MID"
            },
            {
                "offset": "2",
                "proportion": "2",
                "reference": "PEGGED_REFERENCE_MID"
            }
        ],
        "sells": [
            {
                "offset": "1",
                "proportion": "1",
                "reference": "PEGGED_REFERENCE_MID"
            },
            {
                "offset": "2",
                "proportion": "2",
                "reference": "PEGGED_REFERENCE_MID"
            },
            {
                "offset": "5",
                "proportion": "5",
                "reference": "PEGGED_REFERENCE_MID"
            }
        ]
    },
    "pubKey": pubkey,
    "propagate": True
}

print("Liquidity provision submission: ", json.dumps(submission, ensure_ascii=True, indent=4))

# Sign the transaction with a liquidity provision submission
url = f"{wallet_server_url}/api/v1/command/sync"
response = requests.post(url, headers=headers, json=submission)

print("Signed liquidity commitment and sent to Vega")
print(response.json())

exit(0)
time.sleep(10)


#####################################################################################
#               A M E N D    L I Q U I D I T Y   C O M M I T M E N T                #
#####################################################################################

# Compose a liquidity commitment order message
# (it will now serve as an amendment request):
# modify fields you want to be amended
submission = {
    "liquidityProvisionAmendment": {
        "marketId": marketID,
        "commitmentAmount": "500",
        "fee": "0.005",
        "buys": [
            {
                "offset": "1",
                "proportion": "1",
                "reference": "PEGGED_REFERENCE_MID"
            }
        ],
        "sells": [
            {
                "offset": "1",
                "proportion": "1",
                "reference": "PEGGED_REFERENCE_MID"
            }
        ]
    },
    "pubKey": pubkey,
    "propagate": True
}

print("Liquidity provision amendment: ", json.dumps(submission, ensure_ascii=True, indent=4))

# Sign the transaction with a liquidity provision submission command
url = f"{wallet_server_url}/api/v1/command/sync"
response = requests.post(url, headers=headers, json=submission)

print("Signed liquidity commitment (amendment) and sent to Vega")
print(response.json())

# Completed.