# https://github.com/gradoj/nanoserver
# nanoserver.py

from cmac import CMAC

def aesEncrypt(key, data, mode=None):
    """AES encryption function
    
    Args:
        key (str): packed 128 bit key
        data (str): packed plain text data
        mode (str): Optional mode specification (CMAC)
        
    Returns:
        Packed encrypted data string
    """
    dataorder='big'
    keyorder='big'
    
    if mode == 'CMAC':
        cipher = CMAC()
        
        key=(int.from_bytes(key[0:4], 'big'),
             int.from_bytes(key[4:8], 'big'),
             int.from_bytes(key[8:12], 'big'),
             int.from_bytes(key[12:16], 'big'))
        #print(hexlify(key[0].to_bytes(4,byteorder='little')))
        #print(hexlify(key[1].to_bytes(4,byteorder='little')))
        #print(hexlify(key[2].to_bytes(4,byteorder='little')))
        #print(hexlify(key[3].to_bytes(4,byteorder='little')))
        if len(data) <= 16:
            length=len(data)*8
            data=data+bytearray((16-len(data)))
            data=[(int.from_bytes(data[0:4], 'big'),
                   int.from_bytes(data[4:8], 'big'),
                   int.from_bytes(data[8:12], 'big'),
                   int.from_bytes(data[12:16], 'big'))]
                  
        elif len(data) > 16:
            length = (len(data)-16)*8
            data=data+bytearray((32-len(data)))
            data=[(int.from_bytes(data[0:4], 'big'),
                   int.from_bytes(data[4:8], 'big'),
                   int.from_bytes(data[8:12], 'big'),
                   int.from_bytes(data[12:16], 'big')),
                  (int.from_bytes(data[16:20], 'big'),
                   int.from_bytes(data[20:24], 'big'),
                   int.from_bytes(data[24:28], 'big'),
                   int.from_bytes(data[28:32], 'big'))]          
        else:
            print('Data greater than 32 bytes')

        #print('Length', length)
        mic=cipher.cmac(key, data, length)
        
        # Create AES cipher using key argument, and encrypt data
        '''cipher = CMAC.new(key, ciphermod=AES)
        cipher.update(data)
        mic=cipher.hexdigest()
        '''
        #print('MIC',hexlify(bytearray.fromhex(mic)))

        #print(hexlify(mic[0].to_bytes(4,byteorder='little')))
        #print(hexlify(mic[1].to_bytes(4,byteorder='little')))
        #print(hexlify(mic[2].to_bytes(4,byteorder='little')))
        #print(hexlify(mic[3].to_bytes(4,byteorder='little')))
        
        #mic = mic[0].to_bytes(4, 'big')
        mic = mic[0].to_bytes(4, 'big') + mic[1].to_bytes(4, 'big') + mic[2].to_bytes(4, 'big') + mic[3].to_bytes(4, 'big')
        return mic# bytearray.fromhex(mic[0])
        #return bytearray.fromhex(mic)
    else: #if mode == None:
        try: 
            cipher = AES.new(key,AES.MODE_ECB)
        except:
            cipher = AES(key,AES.MODE_ECB)
        return cipher.encrypt(data)
