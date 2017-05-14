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


'''
This function is used to output a 
sorted path array, since I want to measure 
point by point
'''

def sortlistdir(dirnamepath):
    files = glob(dirnamepath)
    a = []
    for item in range(1,len(files)+1):
    	a.append(dirnamepath[:-5] + str(item) + ".txt")
    return a

'''
This function is used to find the nth occurance of needle in
the haystack, mainly use this to find hallwayname or point name
'''


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


'''
This function is used to list all the txt files under on directory
and its subdirectory. Kinda like traverse or walk
'''

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
        	if(not name.startswith('.')):
        		r.append(os.path.join(root, name))
    return r

t = time()


rootdir = '/Users/Qian/Desktop/wifidata'

# This is about the margin of hallwaypoint
# say the ground truth is 5 and threshold is 2
# then as long as the result is 3~7, it will be regarded
# as correct.
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
			#Here 3 is the inner threshold for signal strength, same story as hallway point.
			if (iname == jname and (jvalue - 3 <= ivalue and ivalue - 3 <= jvalue )):
				cad.append(jdata[2])
	# utlize counter function to give confident score
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

# For the whole testing result please check threshold_res.xlsx
