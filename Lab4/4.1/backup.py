import random

from sympy import gcd


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


    # p=random.randint(0,100)
    # q=random.randint(0,100)
    p=5
    q=7


    n=p*q

    ph1=phi(n)


    c=3

    d=inverseModulo(c,ph1)
    print("Public key: ",c)
    print("Mod: ",n)
    print("Input your number")
    msg=input()
    msg=int(msg)
    enctext= pow1(msg,c,n)%n
    print("Encrypted msg: ",enctext)
    dectext= pow1(enctext,d,n)%n
    print("Decrypted msg: ",dectext)
    print(dectext)


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

    # for i in range(0, len(primeList)):
    #     print(primeList[i])





primeGenerate()
rsa()
