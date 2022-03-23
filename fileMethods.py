import os

def clear():
    os.system('cls')

def addToFile(fileName, stringIn):
    f = open(fileName, 'a')
    f.write(stringIn)
    f.write('\n')
    f.close()

def eraseFile(fileName):
    f = open(fileName, 'w')
    f.close()

def printFile(fileName):
    f = open(fileName, 'r')
    for line in f:
        print(line, end='')
    f.close()
