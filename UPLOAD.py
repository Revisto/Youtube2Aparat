from _C_ import *

while True:
    try:
        Full_Programs().AutoVideoUpload()  
        sleep(15*60)
    except Exception as e:
        Telegram().SendNakedMessage('an Error  -------  '+str(e))