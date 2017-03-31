f = open("data_filtered.txt",'r')
g = open("delete.txt",'r')
h = open("copy.txt",'a')

f_r = f.readlines()
g_r = g.readlines()
print(type(f_r))


d=[]

for name in g_r:
	if (name != ' '):
		d.append(name[:17])

#print(d)

for item in f_r:
	cp = (item.split('\t'))[1]
	print(cp)
	
	if (cp not in d):
		h.write(item)
