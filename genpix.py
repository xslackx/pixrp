import pixstatic
from dotenv import dotenv_values

secret = { **dotenv_values('.env') }

def tx_user(txid, value):
    return pixstatic.EMVStatic(secret["PNAME"], secret["PCITY"], txid, secret["PKEY"], value).gen()
