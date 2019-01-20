from Crypto.Cipher import AES

def main():
    f1 = open("aes_ciphertext.hex", "r")
    f2 = open("aes_iv.hex", "r")
    f3 = open("aes_key.hex", "r")

    aes_cipher=f1.read().decode("hex")
    aes_iv=f2.read().decode("hex")
    aes_key=f3.read().decode("hex")
    print(len(f3.read()))

    print(len(aes_key))

    obj=AES.new(aes_key,AES.MODE_CBC,aes_iv)
    result=obj.decrypt(aes_cipher)
    print(result)

    f = open("solution02.txt", "w")
    f.write(result)


if __name__ == "__main__":
    main()