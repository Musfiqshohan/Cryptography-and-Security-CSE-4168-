import random

from sympy import gcd
#https://www.ti89.com/cryptotut/rsa3.htm

def phi(n):
    cop=0
    for i in range(1,n):
        if(gcd(n,i)==1):
            cop=cop+1
    return cop


def inverseModulo(c, n):
    ph=phi(n)


    d=pow1(c,ph-1,n)%n
    return d


def pow1(x,n,mod):
    if(n==0):
        return 1
    if(n%2==0):
        sum=pow1(x,n/2,mod)
        return (sum*sum)%mod
    else:
        return (x*pow1(x,n-1,mod))%mod


def rsa():




    global primeList

    p=primeList[0]
    q=primeList[0]

    while(p*q<100):
        p=primeList[random.randint(0,50)]
        q=primeList[random.randint(0,50)]



    n=p*q
    print("P=",p," Q=",q, "N=",n)

    ph1=phi(n)


    c=3
    for i in range(1, len(primeList)):
        # print(primeList[i],n)
        # print(primeList[i],ph1)
        if(gcd(primeList[i],ph1)==1):
            c=primeList[i]
            break

    d=inverseModulo(c,ph1)
    print("Public key: ",c)
    print("Private key: ",d)
    print("Mod: ",n)

    while(True):
        print("Input your number")
        msg=input()
        msg=int(msg)
        enctext= pow1(msg,c,n)
        # enctext= pow(msg,c)%n
        print("Encrypted msg: ",enctext)
        dectext= pow1(enctext,d,n)
        # dectext= pow(enctext,d)%n
        print("Decrypted msg: ",dectext)
        print(dectext)



#
primeList=[]
def primeGenerate():

    primes=[]

    for i in range(0,100009):
        primes.append(0)


    for i in range(2,1000):
        if(primes[i]==0):
            j=i
            while(i*j<=100000):
                primes[i*j]=1
                j=j+1
    global primeList

    for i in range(2,100000):
        if(primes[i]==0):
            primeList.append(i)

primeGenerate()
rsa()
