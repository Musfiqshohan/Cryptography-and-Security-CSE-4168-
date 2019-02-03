import shlex
import subprocess


from os import system

def main():
    command=""
    for i in range(0,64):
        filename="file"+str(i)+".py"
        output=subprocess.check_output(["python", filename])    #runs "python filename" for 64 files and gets sha output
        c = 'if sha=="'+output.decode("utf-8").strip()+'":\n' + '\tprint("Shohan ' + str(i) + '")\n'
        command += c                    #prints each file with correct condition with individual sha


    print(command)





def addSuffix2():  # concates the suffix 2 which includes all conditions is concatenated with current file
    curFiles=32
    for i in range(0, curFiles):
        newnewFilename = "file0" + str(i * 2) + ".py"
        fx = open(newnewFilename, "wb")
        newFilename = "file" + str(i * 2) + ".py"
        system("cat " + newFilename + " suffix2 > " + newnewFilename)

        newnewFilename = "file0" + str(i * 2 + 1) + ".py"
        fx = open(newnewFilename, "wb")
        newFilename = "file" + str(i * 2 + 1) + ".py"
        system("cat " + newFilename + " suffix2 > " + newnewFilename)




if __name__ == '__main__':
    main()
    # addSuffix2()  # call this commenting main()
