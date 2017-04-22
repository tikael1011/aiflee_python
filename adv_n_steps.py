'''
the purpose of this python script is to take advantage of continous inputs
and get a overall high ranking
first test version is base on n_steps and apply a filter to it.
'''

#UTF-8 Jie

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

innerthreshold = input("Input innerthreshold: ")
outterthreshold = input("Input outerthreshold: ")

<<<<<<< Updated upstream
n_steps = 2
=======
#n_steps = int(input("Input how many steps: "))

n_steps = 2

>>>>>>> Stashed changes
dic = []


file_open = open('data_filtered.txt','r')
all_data = [x.strip() for x in file_open.readlines()]
path = list_files(rootdir)

# print(type(path))
# print(path)


while(n_steps > 1):

	rt = 0
	total = 0

	for txtfile in path:
		startindex = find_nth(txtfile, '/', 6)
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
				if (iname == jname and (jvalue - float(innerthreshold) <= ivalue and ivalue - float(innerthreshold) <= jvalue )):
					cad.append(jdata[2])

		# result = [loc for loc, count in Counter(cad).most_common(3)]

		# point = int((' '.join(result)).split('.')[1])
		#print(point)
		#print("Cal" + " " + txtfile + " " + ' '.join(result))	
		# if(point >= int(txtfile[startindex+1:-4]) - int(outterthreshold) and point <= int(txtfile[startindex+1:-4]) \
		# 	+ int(outterthreshold)):
		# 	rt = rt + 1
		# total = total + 1
		# input_open.close()

		try:
			input_2 = open((txtfile[:startindex+1]+str(int(txtfile[startindex+1:-4]) + 1))+'.txt')
			all_input_2 = [x.strip() for x in input_open.readlines()]
			cad_2 = []
			j = 0
			for element_2 in all_input_2:
				if(element_2 == ""): continue
				if(element_2 == '****####****'): break
				if (j >= 20): break
				idata_2 = element_2.split()
				#print(idata)
				
				iname_2 = idata_2[0]
				ivalue_2 = int(idata_2[3]) # was 1 for the training data and float cast
				if (ivalue_2 <= -85.0):
					continue
				j = j + 1
				for base_2 in all_data_2:
					jdata_2 = base_2.split(',')
					jname_2 = jdata_2[0]
					jvalue_2 = float(jdata_2[1])
					if (iname_2 == jname_2 and (jvalue_2 - float(innerthreshold) <= ivalue_2 and ivalue_2 - float(innerthreshold) <= jvalue )):
						cad_2.append(jdata_2[2])

			for x in cad:
				cad_2.append(x)
			result = [loc for loc, count in Counter(cad_2).most_common(1)]

			point = int((' '.join(result)).split('.')[1])
			#print(point)
			print("Cal" + " " + txtfile[find_nth(txtfile, '/', 5) + 1:find_nth(txtfile, '/', 6)] + \
				"." + txtfile[find_nth(txtfile, '/', 6) + 1:-4] + "&&" + str(int(txtfile[startindex+1:-4]) + 1) + \
				" " + ' '.join(result))	
			if(point >= int(txtfile[startindex+1:-4]) - int(outterthreshold) and point <= int(txtfile[startindex+1:-4]) \
				+ int(outterthreshold) + 1):
				rt = rt + 1
			total = total + 1
			input_open.close()
		except:
			continue
	n_steps = n_steps-1


print(total)
print(rt)
print(rt/total)
print(time()-t)

