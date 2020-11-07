#! python3
# 14.1

import os
def getFilesCurrentDir():
    print(os.listdir())

getFilesCurrentDir()

#14.2
def getFilesParentDir():
    print(os.listdir('..'))

getFilesParentDir()


#14.3
def writeText(text: str, filename: str):
    t = text
    temp = open(filename + ".txt", "w")
    temp.write(t)
    temp.close

writeText('This is a test of the emergency text system', 'test')

#14.4
file = open("test.txt")
test2 = file.read()
print(test2)