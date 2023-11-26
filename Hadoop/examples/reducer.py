#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_count = 0
word = None
#Codigo basado en lo obtenido de ayudantia

count_file = -1
files = {}
# palabra = {1:89}
for line in sys.stdin:

    l = line.strip()
    word, num = l.split("\t",1)
    if(word in files):
        if(num in files[word]):
            files[word][num] += 1
        else:
            files[word][num] = 1
    else:
        files[word] = {num:1}

f = open("output.txt", "w")
f.write("Palabra\t(Archivo, Cantidad)\n")
for word in files:
    f.write(word+"\t")
    x = ""
    for file in files[word]:
        f.write("("+str(file)+","+str(files[word][file])+")"+" ") 
        x = "("+str(file)+","+str(files[word][file])+")"+" "
        print(word+"\t"+x)
    f.write("\n")
f.close()
