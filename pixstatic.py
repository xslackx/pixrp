from dataclasses import dataclass
from crc16 import ccitt
from consts import ( PAYLOADINDICATOR, 
MERCHANTACCOUNT, MERCHANTCATCODE, 
COUNTRYCODE, TXCURRENCY, 
MAXNAMEMERCHANT, MAXTID, 
MAXPIXID, BCB)

@dataclass
class EMVStatic:
    def __init__(self, name, city, txid, key) -> None:
        #PixKey
        self.PK = key[:MAXPIXID]
        
        #PayloadFormatIndicator
        self.PFI = PAYLOADINDICATOR
        
        #MerchantAccountInformation
        self.MAI = MERCHANTACCOUNT
        self.MAIH1 = f'{BCB}{len(self.PK)}{self.PK}'
        self.MAI += f'{len(self.MAIH1)}{self.MAIH1}'
        
        #MerchantCategoryCode
        self.MCC = MERCHANTCATCODE
        
        #TransactionCurrency
        self.TC = TXCURRENCY
        
        #CountryCode
        self.CC = COUNTRYCODE
        
        #MerchantName
        self.MN = name[:MAXNAMEMERCHANT]
        self.sizeMN = len(self.MN)
        if self.sizeMN <= 9:
            self.MN = f'0{self.sizeMN}{self.MN}'
        else:
            self.MN = f'{self.sizeMN}{self.MN}'
        self.MNH = f'59{self.MN}'
        
        #MerchantCity
        if len(city) <= 9:
            self.MC = f'600{len(city)}{city}'
        else:
            self.MC = f'60{len(city)}{city}'
            
        #AdditionalDataFieldTemplate
        if len(txid) <= 9:
            self.TXID = f'050{len(txid[:MAXTID])}{txid[:MAXTID]}'
        else:
            self.TXID = f'05{len(txid[:MAXTID])}{txid[:MAXTID]}'
        self.ADFT = f'62{len(self.TXID)}{self.TXID}'
        
        #CRC16Header
        self.CRC = '6304'
        
    def raw(self):
        return self.PFI+self.MAI+self.MCC+self.TC+\
            self.CC+self.MNH+self.MC+self.ADFT+self.CRC
        
    def gencrc(self):
        return hex(ccitt(polynomial=0x11021,
                        initial_value=0xFFFF,
                        xor_out=0x0000,
                        data=str(self.raw()).encode()
                        )
                  )
    
    def gen(self):
        return self.raw()+self.gencrc()[2:].upper()   
