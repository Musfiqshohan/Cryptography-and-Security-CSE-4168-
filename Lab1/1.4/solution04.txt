from Crypto.Cipher import AES
import codecs

def main():




    f1 = open("substitution_ciphertext.txt", "r")

    cipher=f1.read()


    mn = 10000000000
    mntext = ""

    for i in range(0,26):
        d,str=decrypt(i,cipher)
        if(d<mn):
            mn=d
            mntext=str

    print(mn, mntext)



def decrypt(shift, cipher):


    isLarge=0
    result=""
    for ch in cipher:

        # print(ord('a'),ch,ord(ch))
        dif=0
        if(ch>='A' and ch<='Z'):
            isLarge=1
            dif = ord(ch) - ord('A') + 1
        elif(ch>='a' and ch<='z'):
            dif=ord(ch)-ord('a')+1
        # print(dif)
        dif=(dif+shift)%26
        dif=(dif-1+26)%26

        if (ch >= 'A' and ch <= 'Z'):
            dif = dif + ord('A')
        elif (ch >= 'a' and ch <= 'z'):
            dif = dif + ord('a')


        # dif=dif+ord('a')
        if((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):
            result= result+ chr(dif)
        else:
            result=result+ch




    d=chiSquare(result,isLarge)
    print(d,result)
    return d,result






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













