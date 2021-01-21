import threading
import cryptomath
import sys, random
from socket import *
import csv


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


def skt_server(port=0, format=''):
    myHost = '127.0.0.1'  # '' = all available interfaces on host
    myPort = port  # listen on a non-reserved port number
    with socket( AF_INET, SOCK_STREAM ) as sockobj:  # make a TCP socket object
        sockobj.bind( (myHost, myPort) )  # bind it to server port number
        sockobj.listen()  # listen, allow 5 pending connects
        connection, address = sockobj.accept()  # wait for next client connect
        with connection:
            while True:
                data = connection.recv( 1024 )
                if not data:
                    break
                from struct import unpack
                message = unpack( format, data )


def skt_client(port=0, format='', message=''):
    HOST = '127.0.0.1'  # server name, or: 'starship.python.net'
    PORT = port  # non-reserved port used by the server
    with socket( AF_INET, SOCK_STREAM ) as s:
        s.connect( (HOST, PORT) )
        from struct import pack
        data = pack( format, message )
        s.sendall(data)



SYMBOLS = """ !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main(myMode, myKey, myMessage):

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    return translated


def getKeyParts(key):

    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):

    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
#    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
#        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):

    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''

    for symbol in message:
        if symbol in SYMBOLS:

            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol # just append this symbol unencrypted
    return ciphertext


def decryptMessage(key, message):

    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol

            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext


def getRandomKey():

    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


##  Function that writes the value of *args, **kwargs to a binary file
##  fmt = '' is for the data types being packed, ie: "ffi" denotes three
##  parameters of a float, a float, and an integer. List of data types below.

def write_binary_file(fmt='', filename='',*args, **kwargs):
    from struct import Struct
    mystruct = Struct(fmt)
    data = mystruct.pack(*args, **kwargs)
    with open(filename, "wb") as out:
        out.write(data)

## Reads the binary file and upacks the data

def read_binary_file(fmt='', filename=''):
    from struct import Struct
    fp = open(filename, "rb").read()
    mystruck = Struct(fmt)
    data = mystruck.unpack(fp)
    return data


def write_json_file(filename, data):
    import json
    with open(filename, "a") as file:
        json.dump(data, file)


def write_txt_file(filename='', txt='', option="a"):
    with open(filename, option) as file:
        file.write('\n')
        file.write(txt)


def read_txt_file(filename=''):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def write_csv_file(filename='', option="w"):
    with open(filename, option) as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rows)


def write_key(fmt='', filename='', *args):
    write_binary_file(fmt, filename, *args) 

write_key('i', 'DATA/owm.bin', 2111)
## Clandestine pass of key used to decrypt encoded API_ID to user file

def read_key(fmt='', filename=''):
    key = read_binary_file(fmt, filename)
    mykey = int((key)[0])
    return mykey













if __name__ == "__main__":
    main()
