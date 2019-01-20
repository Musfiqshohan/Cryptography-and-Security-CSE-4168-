from Crypto.Cipher import AES
import codecs

fi = open("aes_weak_ciphertext.hex","r")
ciphertext = fi.readline()
decode_ciphertext = codecs.decode(ciphertext,"hex")
fi.close()

iv = "00000000000000000000000000000000"
decode_iv = codecs.decode(iv,"hex")
keybase = "00000000000000000000000000000000000000000000000000000000000000"
print(keybase.length)

for it in range(0,10):
    key = keybase+ "0" + str(it)
    print(key)
    key = codecs.decode(key,"hex")
    cipher = AES.new(key,AES.MODE_CBC,decode_iv)
    ans = cipher.decrypt(decode_ciphertext)
    print(ans.decode())

for it in range(ord("A"), ord("G")):
    key = keybase + "0" + str(it)
    print("llll")
    print("kkk " ,key)
    key = codecs.decode(key, "hex")
    cipher = AES.new(key, AES.MODE_CBC, decode_iv)
    ans = cipher.decrypt(decode_ciphertext)
    print(ans.decode())

for it in range(0, 10):
    key = keybase + "1" + str(it)
    print(key)
    key = codecs.decode(key, "hex")
    cipher = AES.new(key, AES.MODE_CBC, decode_iv)
    ans = cipher.decrypt(decode_ciphertext)
    print(ans.decode())

for it in range(ord("A"), ord("G")):
    key = keybase + "1" + str(it)
    print(key)
    key = codecs.decode(key, "hex")
    cipher = AES.new(key, AES.MODE_CBC, decode_iv)
    ans = cipher.decrypt(decode_ciphertext)
    print(ans.decode())

print(decode_iv)

