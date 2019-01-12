__author__ = 'saleh'
import os
def countword(filename):
    numwords = 0
    numchars = 0
    numlines = 0
    with open(filename, 'r') as file:
        for line in file:
            wordlist = line.split()
            numlines +=1
            numwords +=len(wordlist)
            numchars +=len(line)
    print("word:", numwords)
    print("lines:", numlines)
    print("charecters:", numchars)
if __name__ == '__main__':

    countword('your_file.txt')