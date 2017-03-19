import re
from collections import Counter
from time import time

t = time()

file_open = open('name.txt','r')
input_open = open('demo.txt','r')
all_data = [x.strip() for x in file_open.readlines()]
all_input = [x.strip() for x in input_open.readlines()]

cad = []

for element in all_input:
	if (i >= 20): break
	idata = element.split(' ')
	iname = idata[0]
	ivalue = float(idata[1])
	if (ivalue <= -85.0):
		continue
	i = i+ 1
	for base in all_data:
		jdata = base.split(',')
		jname = jdata[0]
		jvalue = float(jdata[1])
		if (iname == jname and (jvalue-2 <= ivalue and ivalue-2 <= jvalue )):
			cad.append(jdata[2])

result = [loc for loc, count in Counter(cad).most_common(1)]
print(result)
print(time()-t)
