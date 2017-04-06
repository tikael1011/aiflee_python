import os
import os.path
from collections import Counter
import glob

#flag = True


file_open = open('/home/student/data_filtered.txt','r')
input_path = glob.glob('*.txt')

all_data = [x.strip() for x in file_open.readlines()]



for files in input_path:
	cad = []
	i = 0
	f = open(files,'r')
	input_info = [x.strip() for x in f.readlines()]
	for element in input_info:
		if (i >= 20): break
		idata = element.split(',')
		iname = idata[0]
		ivalue = int(idata[1])
		if (ivalue <= -85.0):
			continue
		i = i + 1
		for base in all_data:
			jdata = base.split(',')
			jname = jdata[0]
			jvalue = float(jdata[1])
			if (iname == jname and (jvalue-2 <= ivalue and ivalue-2 <= jvalue )):
				cad.append(jdata[2])

	result = [loc for loc, count in Counter(cad).most_common(1)]
	o = open('/home/student/location/'+files,'a')
	o.write(result[0])
	f.close()
	o.close()
