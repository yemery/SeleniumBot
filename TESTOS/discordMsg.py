

import requests
from  Scrap  import res

def SendMsg():
        payload={
            "content":'schedule has been changed , Go check it'
        }
        header={
           "authorization":"OTE3ODYwMTM4NTc1MTAyMDMy.GlM0pX.3_4PcqxUfBkH-N7yKuv7AKXWCczRXA8tZHMuag"
        }
        requests.post("https://discord.com/api/v9/channels/928725601546813513/messages",data=payload,headers=header)
    
if(res==True):
    SendMsg()