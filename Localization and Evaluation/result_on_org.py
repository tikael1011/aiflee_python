#UTF-8 Jie

import os
import os.path
import statistics
import math

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import tkinter as tk

from collections import Counter
from time import time
from glob import glob

#### PASS ####

#flag = True


# while(flag):
# 	while(1):

		# hallwayname = input("Input hallwayname or Type exit to exit: ")


		# if(hallwayname.lower() == 'exit'):
		# 	flag = False
		# 	break
		# locationname = input("Input datalocation: ")
#try:
# 	input_open = open('/Users/Qian/Desktop/wifidata/'+ hallwayname +'/'+locationname+".txt",'r')
# except:
# 	print("point does not exist, please try again")
# 	break
def sortlistdir(dirnamepath):
    files = glob(dirnamepath)
    a = []
    for item in range(1,len(files)+1):
    	a.append(dirnamepath[:-5] + str(item) + ".txt")
    return a


flag = True

while(flag):
	while(1):

		hallwayname = input("Input hallwayname or Type exit to exit: ")
		if(hallwayname.lower() == 'exit'):
			flag = False
			break

		path = sortlistdir('/Users/Qian/Desktop/wifidata/' + hallwayname + '/*.txt')
		start_index = len('/Users/Qian/Desktop/wifidata/' + hallwayname)

		file_open = open('data_filtered.txt','r')
		all_data = [x.strip() for x in file_open.readlines()]

		error_all = []

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
					if (iname == jname and (jvalue-3 <= ivalue and ivalue-3 <= jvalue )):
						cad.append(jdata[2])

			result = [loc for loc, count in Counter(cad).most_common(1)]
			print(' '.join(result) + "  " + "And the result should be " + hallwayname + ' ' + txtfile[35:-4])



#file_open = open('data_filtered.txt','r')
#input_open = open('demo.txt','r')




#print(type(all_input))


