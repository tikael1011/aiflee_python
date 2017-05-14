#UTF-8 Jie

'''
This is about the basic footprint method to evaluate
accuray, results includes several parameters.
Will have details below
'''


import os
import statistics
import math

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import tkinter as tk

from collections import Counter
from time import time
from glob import glob


def sortlistdir(dirnamepath):
    files = glob(dirnamepath)
    a = []
    for item in range(1,len(files)+1):
    	a.append(dirnamepath[:-5] + str(item) + ".txt")
    return a

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
        	if(not name.startswith('.')):
        		r.append(os.path.join(root, name))
    return r

t = time()


rootdir = '/Users/Qian/Desktop/wifidata'


threshold = input("Input threshold: ")


file_open = open('data_filtered.txt','r')
all_data = [x.strip() for x in file_open.readlines()]
path = list_files(rootdir)

rt = 0
total = 0


for txtfile in path:
	input_open = open(txtfile,'r')
	all_input = [x.strip() for x in input_open.readlines()]
	cad = []
	i = 0
	for element in all_input:
		if(element == ""): continue
		if(element == '****####****'): break
		if (i >= 20): break
		idata = element.split()
		#print(idata)
		
		iname = idata[0]
		ivalue = int(idata[3]) # was 1 for the training data and float cast
		if (ivalue <= -85.0):
			continue
		i = i + 1
		for base in all_data:
			jdata = base.split(',')
			jname = jdata[0]
			jvalue = float(jdata[1])
			if (iname == jname and (jvalue - 3 <= ivalue and ivalue - 3 <= jvalue )):
				cad.append(jdata[2])

	result = [loc for loc, count in Counter(cad).most_common(1)]
	startindex = find_nth(txtfile, '/', 6)
	point = int((' '.join(result)).split('.')[1])

	print("Cal" + " " + txtfile + " " + ' '.join(result))	
	if(point >= int(txtfile[startindex+1:-4]) - int(threshold) and point <= int(txtfile[startindex+1:-4]) + int(threshold)):
		rt = rt + 1
	total = total + 1
	input_open.close()


print(total)
print(rt)
print(rt/total)
print(time()-t)


#776 total, 677rt, 0.8724226804123711 with threshold 3
#665rt, 0.8569587628865979 with threshold 2
#687rt, 0.8853092783505154 with threshold 4
#623, with th1
#514, with th0

#inner thres from 0~3

#file_open = open('data_filtered.txt','r')
#input_open = open('demo.txt','r')


#print(type(all_input))
