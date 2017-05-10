import os
import statistics
import math

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

def hallwaypoint_to_crd(hwp):
	crd = open('hallway_cod.txt','r')
	crd_base = [x.strip() for x in crd.readlines()]
	for ref in crd_base:
		name = ref.split(',')
		if(name[0] == hwp):
			tmp = []
			tmp.append(name[1])
			tmp.append(name[2])
			crd.close()
			return tmp

#print(type(hallwaypoint_to_crd('v10.1')))


def cal_dis(x,y):
	return math.sqrt((float(x[0]) - float(y[0])) ** 2 + (float(x[1]) - float(y[1])) ** 2)


def del_outlyer(inputlist):
	p0 = hallwaypoint_to_crd(inputlist[0])
	p1 = hallwaypoint_to_crd(inputlist[1])
	p2 = hallwaypoint_to_crd(inputlist[2])
	d0 = cal_dis(p0,p1)
	d1 = cal_dis(p1,p2)
	d2 = cal_dis(p2,p0)
	if (abs(d0 - d1) > 5) and (abs(d2 - d1) > 5):
		del inputlist[0]
		return inputlist
	elif (abs(d0 - d2) > 5) and (abs(d2 - d1) > 5):
		del inputlist[2]
		return inputlist
	elif (abs(d1 - d2) > 5) and (abs(d0 - d2) > 5):
		del inputlist[1]
		return inputlist
	else:
		return inputlist
#print(cal_dis([0,4],[3,0]))


innerthreshold = float(input("Input innerthreshold: "))
outterthreshold = int(input("Input outerthreshold: "))
steps = int(input("Input steps: "))
#disthreshold = float(input("Input disthreshold: "))

t = time()

rootdir = '/Users/Qian/Desktop/wft'


crd = open('hallway_cod.txt','r')
crd_base = [x.strip() for x in crd.readlines()]
for ref in crd_base:
	name = ref[0]
file_open = open('data_filtered.txt','r')
all_data = [x.strip() for x in file_open.readlines()]
path = list_files(rootdir)

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
		
		iname = idata[0]
		ivalue = int(idata[3])
		if (ivalue <= -85.0):
			continue
		i = i + 1
		for base in all_data:
			jdata = base.split(',')
			jname = jdata[0]
			jvalue = float(jdata[1])
			if (iname == jname and (jvalue - innerthreshold <= ivalue and ivalue - innerthreshold <= jvalue )):
				cad.append(jdata[2])

	cnt = []
	cnt = Counter()
	hpcd = []
	for element in cad:
		cnt[element] += 1

	print(cnt)

	for k,v in cnt.most_common(3):
		hpcd.append(k)
	input_1 = del_outlyer(hpcd)

	for v in cnt:
		if(v not in input_1):
			del cnt[k]

'''
	while(steps > 1):
		try:
			input_2 = open((txtfile[:startindex+1]+str(int(txtfile[startindex+1:-4]) + steps-1))+'.txt')
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
			cnt_2 = Counter()
			hpcd_2 = []
			for element in cad_2:
				cnt_2[element] += 1
			for k,v in cnt.most_common(3):
				hpcd.append(k)
			input_2 = del_outlyer(hpcd)

			for v in cnt_2:
				if(v not in input_2):
					del cnt_2[k]

			res = (cnt + cnt_2).most_common(1)
			point = int((' '.join(res)).split('.')[1])
			if(point >= int(txtfile[startindex+1:-4]) - int(outterthreshold) and point <= int(txtfile[startindex+1:-4]) \
			+ int(outterthreshold) + 1):
				rt = rt + 1
			total = total + 1
			steps = steps-1
		except:
'''			break

print(total)
print(rt)
print(rt/total)
print(time()-t)
