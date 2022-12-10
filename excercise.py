import os
import sys
import re
import glob
import subprocess
import time, glob

import nltk
nltk.download('punkt')

root='/Users/sachinmishra/Desktop/nyt'
x=os.getcwd()
dir_list=os.listdir()

def f1():
    for i in dir_list:
        try:
            os.chdir(x+'/'+i)
            outfilename = 'all_' + str((int(time.time()))) + ".txt"

            filenames = glob.glob('*.tmp')
            filenames=sorted(filenames)

            with open(outfilename, 'wb') as outfile:
                for fname in filenames:
                    with open(fname, 'r') as readfile:
                        infile = readfile.read()
                        for line in infile:
                            outfile.write(line.encode())
                        #outfile.write("\n".encode())
            
        except Exception as e:
            print(e)
    os.chdir(root)      

def f2():
    for file1 in dir_list:
        try:
            os.chdir(x+'/'+file1)
            files = glob.glob('*.txt')
            for j in files:
                file= open(j,'r',encoding='utf-8')
                text=file.read()
                text=text.replace("\n", "")
                nltk.tokenize.sent_tokenize(text, language='english')

                sentences=sent_tokenize(text)
                final_file= 'final.txt'
                with open(final_file, 'wb') as outfile:
                    for k in sentences:
                        outfile.write(k.encode())
                        outfile.write('\n'.encode())
            
        except Exception as e:
            print(e)
    os.chdir(root)     

