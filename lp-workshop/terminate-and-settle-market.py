#!/usr/bin/python3

import json
import os
import requests
import time
import base64


# EDIT YOUR TERMINATION AND SETTLEMENT VALUES BELOW 

target_settlement_price = 25888 #8441000 (equivalent note dp conversion is automatic below)
target_market_dp = 2
target_dp_converted_price = str(int(target_settlement_price*10**target_market_dp))

target_termination_key = "trading.terminated.BTC2"
target_settlement_key = "prices.BTC2.value"

# END TERMINATION AND SETTLEMENT VALUES


node_url_rest = os.getenv("NODE_URL_REST")
wallet_server_url = os.getenv("WALLETSERVER_URL")
wallet_name = os.getenv("WALLET_NAME")
wallet_passphrase = os.getenv("WALLET_PASSPHRASE")
marketID = os.getenv("VEGA_MARKET")

"""
Settle the market and send settlement price.
"""

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

print("Send oracle to termiate the market.")

# Use oracle to terminate market
payload = {target_termination_key: "true"}
as_str = json.dumps(payload).encode()
oracle = {
    "oracleDataSubmission": {
        "source": "ORACLE_SOURCE_JSON",
        "payload": base64.b64encode(as_str).decode("ascii"),
    },
    "pubKey": pubkey,
    "propagate": True
}

time.sleep(10)
print("sending in settled")

url = f"{wallet_server_url}/api/v1/command/sync"
response = requests.post(url, headers=headers, json=oracle)

print("Signed terminate command and sent to Vega")
print(response.json())

# use oracle to settle market

payload = {target_settlement_key: target_dp_converted_price}
as_str = json.dumps(payload).encode()
oracle = {
    "oracleDataSubmission": {
        "source": "ORACLE_SOURCE_JSON",
        "payload": base64.b64encode(as_str).decode("ascii"),
    },
    "pubKey": pubkey,
    "propagate": True
}

url = f"{wallet_server_url}/api/v1/command/sync"
response = requests.post(url, headers=headers, json=oracle)

print("Signed settle market command and sent to Vega")
print(response.json())