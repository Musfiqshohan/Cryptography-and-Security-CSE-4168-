import hashlib
import shlex
import subprocess

from os import system


def Mash(input):
    m = hashlib.md5()
    m.update(input)
    print(m.hexdigest())

def main():
    curFiles = 2
    subprocess.run(["./fastcoll", "-p", "prefix", "-o", "col0", "col1"])
    while(curFiles<=32):

        subprocess.run(["./fastcoll", "-p", "col0", "-o", "colx", "coly"])

        with open("colx", "rb") as f:
            byte1 = f.read()


        with open("coly", "rb") as f:
            byte2 = f.read()

        newHash1 = []
        newHash2 = []

        L1= len(byte1)
        L2= len(byte2)
        id=1
        while(id!=129):
            newHash1.append(byte1[L1-id])
            id=id+1
        newHash1.reverse()
        # print(newHash1)
        id=1
        while (id != 129):
            newHash2.append(byte2[L2 - id])
            id = id + 1

        newHash2.reverse()


        newHash1 = bytes(newHash1)
        newHash2 = bytes(newHash2)



        hashList={}

        for i in range(0,curFiles):
            filename="col"+str(i)
            with open(filename, "rb") as f:
                prev = f.read()
            newHash1 = bytes(newHash1)
            prev = prev + newHash1
            hashList["col"+str(i*2)]=prev


            filename = "col" + str(i)
            with open(filename, "rb") as f:
                prev = f.read()
            newHash2 = bytes(newHash2)
            prev = prev + newHash2
            hashList["col"+str(i*2+1)] = prev


        for i in range(0, curFiles):
            filename = "col" + str(i * 2)
            f = open(filename, "wb")
            f.write(hashList[filename])

            filename = "col" + str(i * 2 + 1)
            f = open(filename, "wb")
            f.write(hashList[filename])


        curFiles=curFiles*2
    #
    curFiles= int(curFiles/2)

    print("verification")
    for i in range(0,curFiles):

        filename = "col" + str(i * 2)
        print(filename+":")
        f=open(filename,"rb")
        newFilename="file"+str(i * 2)+".py"
        fx = open(newFilename, "wb")

        system("cat "+filename+" suffix1 > "+newFilename)
        inp=f.read()
        Mash(inp)

        filename = "col" + str(i * 2 + 1)
        print(filename+":")
        f = open(filename, "rb")
        newFilename = "file" + str(i * 2+1) + ".py"
        fx = open(newFilename, "wb")

        system("cat " + filename + " suffix1 > "+newFilename)
        inp = f.read()
        Mash(inp)




if __name__ == '__main__':
    main()
    # now run the he 00HelpingFunction function