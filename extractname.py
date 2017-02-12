#utf -8
#Jie Qian
 
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
 
'''
for key,element in obj.items():
    print (type(element))
    result.append(element)
'''
 
o1 = obj[1].intersection(obj[2])
# print(o1)
# allp = set(obj)
# print(allp)
ction(obj[32])
 
print(o31)
 
 
 
 
 
'''
temp = (result[0].intersection(*result[0:]))
 
print(temp)
print(len(temp))
#print(len(result))
#result = list(result)
'''
h = open("apname.txt","wt")
h.write('\n'.join(list(o31)))
 
#print(result)
 
 
# o2 = o1.intersection(obj[3])
# o3 = o2.intersection(obj[4])
# o4 = o3.intersection(obj[5])
# o5 = o4.intersection(obj[6])
# o6 = o5.intersection(obj[7])
# o7 = o6.intersection(obj[8])
# o8 = o7.intersection(obj[9])
# o9 = o8.intersection(obj[10])
# o10 = o9.intersection(obj[11])
# o11 = o10.intersection(obj[12])
# o12 = o11.intersection(obj[13])
# o13 = o12.intersection(obj[14])
# o14 = o13.intersection(obj[15])
# o15 = o14.intersection(obj[16])
# o16 = o15.intersection(obj[17])
# o17 = o16.intersection(obj[18])
# o18 = o17.intersection(obj[19])
# o19 = o18.intersection(obj[20])
# o20 = o19.intersection(obj[21])
# o21 = o20.intersection(obj[22])
# o22 = o21.intersection(obj[23])
# o23 = o22.intersection(obj[24])
# o24 = o23.intersection(obj[25])
# o25 = o24.intersection(obj[26])
# o26 = o25.intersection(obj[27])
# o27 = o26.intersection(obj[28])
# o28 = o27.intersection(obj[29])
# o29 = o28.intersection(obj[30])
# o30 = o29.intersection(obj[31])
# o31 = o30.interse
