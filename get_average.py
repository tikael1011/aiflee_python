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
import xlsxwriter
 
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
 
path = sortlistdir('/Users/Qian/Desktop/wifidata/H_Eight/*.txt')

method = 1 

j = 1

h = open("avg.txt", 'w+')

for txtfile in path:
    f = open(txtfile, 'r')
    g = open('/Users/Qian/Desktop/wifidata/AVG/H8/' + str(j) + '.txt', 'w+')
    #print(f)
    all_lines = f.read()
    content = sorted(all_lines.split("\n"))
    info = []
    d = []
    for sss in content:
    	if (sss[:17] != '' and sss[:17] != '****####****'):
    		info.append(sss[:17])
    info = set(info)
    #print(info)
    
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
            d.append(name + ' ' + str(real_nb) + '\n')
    #g.writelines(d)
    g.writelines(d)
    j += 1
    g.close()
'''
    elif(method == 2):
        for name in info:
            nb = []
            for element in content:
                if (name == element[:17]):
                    nb.append(int(element[-3:])) 
            real_nb = statistics.median(nb)
            (d[j])[name] = real_nb
        j = j + 1
 '''

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column(1, 1, 15)
worksheet.set_column(2, 1, 15)
worksheet.write('A1', 'No')
worksheet.write('B1', 'Ap Name')
worksheet.write('C1', 'Strength')

row = 1
col = 1
point = 1

path2 = sortlistdir('/Users/Qian/Desktop/wifidata/AVG/H8/*.txt')
#print(path2)

for txtfile in path2:
	h = open(txtfile,'r')
	h_txt = h.read()
	info = sorted(h_txt.split("\n"))
	print(info)
	#g = open(txtfile,'w')
	#worksheet.write(row,1,point)
	for line in info:
		if(line == ''): continue
		item = line.split(' ')
		#print(item)
		'''
		if(len(item) != 2):
			print(len(item))
			break
		'''			
		worksheet.write(row,0,point)
		worksheet.write_string(row,col,item[0])
		worksheet.write_number(row,col+1,float(item[1]))
		row = row + 1
	h.close()
	point  = point + 1

workbook.close()
print("done!")

 
print(time()-t)
 
#print(d)
#print (type(d))
 
