# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:57:48 2022

@author: subhr
"""

'   SUBSTUTUTION CIPHER  '
print('Substitution Cipher')


import string
dict={}
data=""
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open ("ip_file.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print('End of the line')
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
        
file.close()



























