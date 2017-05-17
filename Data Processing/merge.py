#utf -8
#Jie Qian
 
import sys
import re
import glob
import itertools
from time import time
from collections import defaultdict
import statistics

 
####Start Main####
# print("1 means linear with power X")
# print("2 means trigonometric func")
# print("3 means ")
# cf = int(input("select curve fitting func: "))

 
####Def Func for Sorting###
def sortlistdir(dirnamepath):
    files = glob.glob(dirnamepath)
    a = []
    for item in range(1,len(files)+1):
    	a.append(dirnamepath[:-5] + str(item) + ".txt")
    return a
 
 
####Creat List from Txt File and Record Time####
t = time()

ad = open("alldata.txt",'a')


path = sortlistdir('/Users/Qian/Desktop/wifidata/AVG/H8/*.txt')

i = 1

for txtfile in path:
    f = open(txtfile, 'r')
    #print(f)
    all_lines = f.read()
    content = sorted(all_lines.split("\n"))
    for sss in content:
    	if (sss[:17] != ''):
    		ad.write('h8.' + str(i) + ' ' + sss + '\n')
    #info = set(info)
    #print(info)
    i += 1
 
print(time()-t)
print('h8')
 
#print(d)
#print (type(d))
 
