# useful links: https://sagi.io/2016/04/crypto-classics-wieners-rsa-attack/?fbclid=IwAR1IP6wHrGQxkI21AHsJfktyKBuCKbjDby1RZOO9txP3sR90zeFs9Evjyhs


import hashlib
from fractions import Fraction
from Crypto.PublicKey import RSA
from sympy import Symbol, solve
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# import vulnerable_key as vk

import math


def do(e,N):

    k=e
    d=N
    values=[]
    cnt=0

    while(d!=0):  # increase here for large numbers!!!!!!!!!!!!!
        cnt=cnt+1

        print(k,d)
        if(d==0):
            return
        div=k//d
        values.append(div)


        if(div!=0):
            res=getfraction(values)
            if(res.denominator%2!=0):
                ret=quadratic_check(e,res.numerator,res.denominator,N)
                if(ret!=-1):
                    return ret



        rem=k%d
        k=d
        d=rem



def quadratic_check(e,k,d,N):
    phi_n= (e*d-1)//k

    p = Symbol('p', integer=True)
    roots = solve(p ** 2 + (phi_n - N - 1) * p + N, p)
    if len(roots) == 2:
        pp, pq = roots  # pp - possible p, pq - possible q
        if pp * pq == N:
            print("FOUND!!!!!!!")
            print('SHA1(p):    ', sha1(pp))
            print('SHA1(q):    ', sha1(pq))
            print("Solution Found:")
            print("p->",pp)
            print("q->",pq)
            print("d->",d)

            return d


    else:
        print("Not found Till now")
        return -1





def getfraction(valuex):

    values=list(valuex)
    for i in range(len(values)-1, 0,-1):
        den=Fraction(1,values[i])
        values[i-1]= values[i-1] + den


    return values[0]

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def sha1(n):
    h = hashlib.sha1()
    h.update(str(n).encode('utf-8'))
    return h.hexdigest()




def getData():
    f = open("4.4_public_key.hex", "r")
    pk = f.read()
    pk = int(pk, 16)

    f = open("4.5_modulo.hex", "r")
    modulo = f.read()
    modulo = int(modulo, 16)

    f = open("4.3_ciphertext.hex", "r")
    cipher = f.read()
    cipher = int(cipher, 16)


    return (pk,modulo,cipher)


def pow1(x,n,mod):

    res=1
    x=x%mod
    while(n):
        if(n%2==0):
            x= (x*x)%mod
            n=n//2
        else:
            res=(res*x)%mod
            n=n-1

    return res


if __name__ == '__main__':

    # N,e,d,p,q = vk.create_keypair(1024)
    # used for short private key pair
    e,N,enctext=getData()
    d=do(e,N)
    dectext = pow1(enctext, d, N)
    print(dectext)





# k =d not possible  since e< phi(N) < N    we know e/N= k/d
# k<d  always
# d can not be 1 cz encrypt =decrypt becomes equal and e=1, then phi(n)=(ed-1)/k=0
# we think, e = d is not possible cz then e= e^( phi(phi(n))-1)   [modular inverse of e =d]
#       so, 1= phi(phi(n))-1   ->phi(phi(n))=2   -> phi(4)=2  and  phi(10)=4
#       so, if e=3, d=3, n=10,p=2,q=5  then no rule is broken but we dont get same result
#       10^3 mod 10 =0