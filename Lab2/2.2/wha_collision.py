import codecs


def main():
    f = open("3.2_input_string.txt", "r")

    inStr=f.read()





    h1=int("0xCC",16)
    h2=int("0x33",16)
    h3=int("0xAA",16)
    h4=int("0x55",16)

    print(h1,h2,h3,h4)

    mask=0x3FFFFFFF
    outhash=0

    for ch in inStr:
        byte = hex(ord(ch))


        dec= int(byte,16)
        i1 = (dec ^ h1) <<24
        i2 = (dec ^ h2) <<16
        i3 = (dec ^ h3) <<8
        i4 = dec ^ h4
        inter= i1 | i2 | i3 | i4

        print(i1,i2,i3,i4)

        outhash= (outhash & mask) + (inter & mask)

    # print(outhash)

    print(hex(outhash))












main()