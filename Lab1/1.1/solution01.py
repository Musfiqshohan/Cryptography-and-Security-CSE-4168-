def main():
    f = open("sub_ciphertext.txt", "r")

    cipher=""
    for x in f:
        cipher+=x


    print cipher

    f = open("sub_key.txt", "r")

    keystr = ""
    i=65
    for x in f:
        keystr=x


    print(keystr)

    key={}
    for i in xrange(0, len(keystr)):
        ch=chr(i+65)
        key[keystr[i]] =ch

        # print(ch,keystr[i])

        i=i+1

    # print(key)


    result=""
    for i in cipher:
        if(i>='A' and i<='Z'):
            # print(key[i], i)
            result+=key[i]
        else:
            result+=" "


    print(result)

    f = open("solution01.txt", "w")


    f.write(result)




if __name__ == "__main__":
    main()