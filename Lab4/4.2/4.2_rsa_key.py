from Crypto.PublicKey import RSA
key = RSA.generate(2048)


with open("private.key", 'wb') as f:
    f.write(key.exportKey('PEM'))

pubkey=key.publickey()
f=open("private.key", 'rb')
privkey=f.read()



msg="hello world"
print("Encrpyted message------>")
encmsg=key.encrypt(msg,privkey)
print(encmsg)
print("Decrpyted message------>")
print(key.decrypt(encmsg))