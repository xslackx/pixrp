from consts import PKEY,PNAME,PCITY
import pixstatic

def tx_user(txid, value):
    return pixstatic.EMVStatic(PNAME, PCITY, txid, PKEY, value).gen()
