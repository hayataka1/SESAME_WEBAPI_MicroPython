import time
import binascii
import requests
import json
from aesEncrypt import aesEncrypt

uuid = '3DE4DE72-AAF9-25C1-8D0F-C9E019BB060C'
secret_key = '2ebc2c087c1501480834538ff72139bc'
api_key = 'SrSOEY9mBe6Ndl7bwyVPs5TsTPFTEq9tra8Occad'

cmd = 88  # 88/82/83 = toggle/lock/unlock
history = 'test5'
base64_history = binascii.b2a_base64(history,newline=False).decode()

print(base64_history)
headers = {'x-api-key': api_key}

ts = time.time() + 946684800   ## ESP8266 Epoch / 946684800 is 2000/01/01 00:00:00 UTC
message = ts.to_bytes(4,'little')
message = binascii.hexlify(message)[2:8]
message = message.decode('utf-8')

cmac = aesEncrypt(bytes.fromhex(secret_key),bytes.fromhex(message),mode='CMAC')
sign = binascii.hexlify(cmac).decode()
# 鍵の操作
url = 'https://app.candyhouse.co/api/sesame2/' + uuid + '/cmd'
body = {
    'cmd': cmd,
    'history': base64_history,
    'sign': sign
}
res = requests.post(url, data = json.dumps(body), headers=headers)
print(res.text)
