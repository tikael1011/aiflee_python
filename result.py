import os
import os.path
from collections import Counter
from time import time
from glob import glob

#### PASS ####
# for dirpath, dirnames, filenames in os.walk("."):
#     for filename in [f for f in filenames if f.endswith(".txt")]:
#         print os.path.join(dirpath, filename)
#### PASS ####

flag = True

'''
while(flag):
	while(1):
'''

'''
hallwayname = input("Input hallwayname or Type exit to exit: ")


if(hallwayname.lower() == 'exit'):
	flag = False
	break
locationname = input("Input datalocation: ")

file_open = open('data_filtered.txt','r')

try:
	input_open = open('/Users/Qian/Desktop/wifidata/AVG/'+hallwayname.upper() +'/'+locationname+".txt",'r')
except:
	print("point does not exist, please try again")
	break
'''
t = time()

file_open = open('data_filtered.txt','r')
input_open = open('/Users/Qian/Desktop/fei/fei5.txt','r')

all_data = [x.strip() for x in file_open.readlines()]
all_input = [x.strip() for x in input_open.readlines()]

cad = []

i = 0

for element in all_input:
	if(element == ""): continue
	if(element == '****####****'): break
	if (i >= 20): break
	idata = element.split()
	iname = idata[0]
	ivalue = int(idata[3]) # was 1 for the training data and float cast
	if (ivalue <= -85.0):
		continue
	i = i + 1
	for base in all_data:
		jdata = base.split(',')
		jname = jdata[0]
		jvalue = float(jdata[1])
		if (iname == jname and (jvalue-2 <= ivalue and ivalue-2 <= jvalue )):
			cad.append(jdata[2])

result = [loc for loc, count in Counter(cad).most_common(5)]
print("Based on the data you input, you are at {}".format(result))
print("Time spent on computation: " + "{:.3f}".format(time()-t) + 's')

####****
# if __name__ == '__main__':
# 	main()
####****
