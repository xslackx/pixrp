from consts import PKEY,PNAME,PCITY
import pixstatic

def tx_user(txid):
    return pixstatic.EMVStatic(PNAME, PCITY, txid, PKEY).gen()
