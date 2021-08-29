#!/usr/bin/python3

from base64 import b64decode, b64encode
from hashlib import sha512

uoption = input("(E)ncode or (D)ecode Message?: ")
cList = []

def encipher(msg, key):
	for i in range(0, len(msg)):
		cList.append(chr(ord(msg[i])^ord(key[i%len(key)])))
	return str(b64encode(''.join(cList).encode()),"utf8")

def decipher(txt, key):
	try:
		msg = b64decode(txt)
	except:
		print("ERROR: Supplied Ciphertext NOT Base64 String")
		exit()

	for i in range(0, len(msg)):
		cList.append(chr(msg[i]^ord(key[i%len(key)])))
	return ''.join(cList)

if uoption.upper() == "E":
	key = sha512(input("Enter Passphrase: ").encode("utf-8")).hexdigest()
	message = input("Enter Message: ")
	print("Encoded Message:")
	print(encipher(message, key))
	
elif uoption.upper() == "D":
	key = sha512(input("Enter Passphrase: ").encode("utf-8")).hexdigest()
	message = input("Ciphertext: ")
	print("Decoded Message:")
	print(decipher(message, key))
	
else:
	print("Invalid Option")
