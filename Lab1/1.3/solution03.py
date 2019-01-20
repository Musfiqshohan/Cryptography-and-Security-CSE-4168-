from Crypto.Cipher import AES
import codecs

def main():
    f1 = open("aes_weak_ciphertext.hex", "r")


    aes_cipher=codecs.decode(f1.read(),"hex")   #read as string then assuming as hex maybe converted to ascii?


    aes_iv=""
    while (len(aes_iv) != 32):
        aes_iv = aes_iv + "0"

    aes_iv = codecs.decode(aes_iv, "hex")          #after converting it gets half, so since 16 byte aes_iv needed
                                                    #so loops to 32

    mn = 10000000000
    mntext = ""

    for i in range(0, 32):



        aes_key="%0.2X" % i
        while (len(aes_key) != 64):     #32 byte key needed so loops to 64
            aes_key = "0" + aes_key


        aes_key=codecs.decode(aes_key,"hex")
        obj = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        result = obj.decrypt(aes_cipher)


        print(result)

        # result=codecs.decode(result,'ASCII')
        # print(type(result))

    #     argStr=result.lower()
    #     d = chiSquare(argStr, 0)
    #     if(d<mn):
    #         mn=d
    #         mntext
    #     print(d,result)
    #
    # print("Output")
    # print(d,mntext)




def chiSquare(text,isLarge):

    prob=make_prob_table()

    if(isLarge==1):
        inc=65
    else:
        inc=97

    freq={}
    for x in range(0,26):
        freq[chr(x+inc)]=0

    for ch in text:
        if ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):
            freq[ch]=freq[ch]+1

    # print(freq)
    return calcValue(freq,prob, len(text),inc)


def calcValue(freq, prob,  L,inc):

    sum=0

    for i in range(0,26):
        C= freq[chr(i+inc)]
        E=L*prob[chr(i+inc)]
        d=C-E
        sum= sum + (d*d)/E


    return sum



def make_prob_table():
    prob={}
    prob['A'] =prob['a']= 8.167
    prob['B'] =prob['b']= 1.492
    prob['C'] =prob['c']=2.782
    prob['D'] =prob['d']=4.253
    prob['E'] =prob['e']=12.702
    prob['F'] =prob['f']=2.228
    prob['G'] =prob['g']=2.015
    prob['H'] =prob['h']=6.094
    prob['I'] =prob['i']=6.996
    prob['J'] =prob['j']=0.153
    prob['K'] =prob['k']=0.772
    prob['L'] =prob['l']=4.025
    prob['M'] =prob['m']=2.406
    prob['N'] =prob['n']=6.749
    prob['O'] =prob['o']=7.507
    prob['P'] =prob['p']=1.929
    prob['Q'] =prob['q']=0.095
    prob['R'] =prob['r']=5.987
    prob['S'] =prob['s']=6.327
    prob['T'] =prob['t']=9.056
    prob['U'] =prob['u']=2.758
    prob['V'] =prob['v']=0.978
    prob['W'] =prob['w']=2.360
    prob['X'] =prob['x']=0.150
    prob['Y'] =prob['y']=1.974
    prob['Z'] =prob['z']=0.074

    return prob




if __name__ == "__main__":
    main()











