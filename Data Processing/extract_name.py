#utf -8
#Jie Qian
'''
This file is used to extract common apname
along the hallway and is used for old algorithm(MATLAB one)
No longer is use
'''


import sys
import re
import glob
import os
import itertools

#vary
path = '/Users/Aeolus/Desktop/sdcard/*.txt' 
files = glob.glob(path)
 
 
obj = {}

#vary in range
for i in range(1,33):
    obj[i] = []
 
 
k = 1
 
for txtfile in files:
    f = open(txtfile,'r')
    g = open(txtfile,'w')
    namelist = []
    all_lines = f.read()
    content = sorted(all_lines.split("\n"))
    #all_str = ''.join(str(element) for element in all_lines)
    #print(all_str)
 
    #content = list(filter (lambda x : not re.match(r'^\s*$', x),all_lines)) # use list may get a better performance, we will see in the future.
    #print(content)
 
    for line in content:
        name = line.split(' ',1)[0]
        namelist.append(name)
 
    obj[k]= set(namelist)
    k = k + 1
f.close()
 
 
result =[]
 

for key,element in obj.items():
    print (type(element))
    result.append(element)

 
#o1 = obj[1].intersection(obj[2])
# print(o1)
# allp = set(obj)
# print(allp)
#ction(obj[32])
 
#print(o31)
 
 
 
 
 

temp = (result[0].intersection(*result[0:]))
 
print(temp)
print(len(temp))
#print(len(result))
#result = list(result)

h = open("apname.txt","wt")
h.write('\n'.join(list(o31)))
 
#print(result)
 
 
