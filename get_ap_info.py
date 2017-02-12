#utf -8
#Jie Qian
 
import sys
import re
import glob
import itertools
from time import time
from collections import defaultdict
import statistics
import json
 
####Start Main####
 
print("1 means average")
print("2 means median")
method = int(input("input method you want: "))
# print("1 means linear with power X")
# print("2 means trigonometric func")
# print("3 means ")
# cf = int(input("select curve fitting func: "))
 
 
####Def Func for Sorting###
def sortlistdir(dirnamepath):
    a = []
    files = glob.glob(dirnamepath)
    #print(files)
    for item in files:
        temp = int(re.search(r'\d+',item).group())
        a.append(temp)
    a.sort()    
    b = []
    for item in a:
        b.append(dirnamepath[:-5] + str(item) + ".txt")
    return b
 
 
####Creat List from Txt File and Record Time####
t = time()
 
path = sortlistdir('/Users/Aeolus/Desktop/sdcard_sort/*.txt')
 
d = [ {} for i in range (1,33)]
 
h = open("apname.txt","r")
h_txt = h.read()
info = sorted(h_txt.split("\n"))
 
j = 0
 
for txtfile in path:
    f = open(txtfile, 'r')
    #print(f)
    all_lines = f.read()
    content = sorted(all_lines.split("\n"))
    if(method == 1):
        for name in info:
            #print(name)
            nb = 0
            count = 0
            for element in content:
                if (name == element[:17]):
                    nb = int(element[-3:]) + nb
                    count = count + 1
            real_nb = nb / count
            (d[j])[name] = real_nb
        j = j + 1
    elif(method == 2):
        for name in info:
            nb = []
            for element in content:
                if (name == element[:17]):
                    nb.append(int(element[-3:])) 
            real_nb = statistics.median(nb)
            (d[j])[name] = real_nb
        j = j + 1
 
     
 
print(time()-t)
 
#print(d)
#print (type(d))
 
'''
for item in d:
    with open("outputfile.txt","a") as f:
        json.dump(item, f)
        f.write('\n')
 
 
with open("tmp2.txt","w") as i:
    json.dump(x,i)
'''
 
ap_all = [ [] for i in range (1,19)]
 
 
 
 
for item in d:
    k = 0
    for key, val in sorted(item.items()):
        ap_all[k].append(val)
        k = k + 1
 
 
#print (ap_all)
 
with open("temp.txt",'wt') as g:
    g.writelines(','.join(str(element) for element in item) + '\n' for item in ap_all)
 
 
 
#print(ap_all)
