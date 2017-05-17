
'''
used ti filter ap name that occurs less than 5 times
There is a better way to implement this
'''
from time import time

t = time()

d = []

f = open("filter.txt",'r')
g = open("delete.txt",'a')
content = f.readlines()
for i in range(0,32220):
	if(content[i] != content[i+1]):
		if(content[i+1] != content[i+2]):
			if(content[i+1] != content[i+3]):
				if(content[i+1] != content[i+4]):
					if(content[i+1] != content[i+5]):
						d.append(content[i+1])
						d.append(content[i+2])
						d.append(content[i+3])
						d.append(content[i+4])

d = sorted(set(d))
for item in d:
	g.write(item)

print(time()-t)
