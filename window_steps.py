import os
import statistics
import math
import operator

from collections import Counter
from time import time
from glob import glob

def sortlistdir(dirnamepath):
    files = glob(dirnamepath)
    a = []
    for item in range(1,len(files)+1):
        a.append(dirnamepath[:-5] + str(item) + ".txt")
    return a

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if(not name.startswith('.')):
                r.append(os.path.join(root, name))
    return r

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def get_hallname(string):
    return (string[find_nth(string,'/',5)+1:find_nth(string,'/',6)])



ref_h = []
ref = []
for dirpath, dirnames, filenames in os.walk("/Users/Qian/Desktop/AVG"):
    for filename in [f for f in filenames if f.endswith(".txt")]:
        ref_h.append(os.path.join(dirpath))

ref_h = list(set(ref_h))
#print(ref_h)

for element in ref_h:
    files = sortlistdir(element+'/*.txt')
    for f in files:
        ref.append(f)
#print('\n'.join(ref))
ref_size = len(ref)

steps = int(input("Input window size: "))

steps_i = steps

database = []

while(steps_i>0):
    database_path = input("Input path: ")
    database.append(database_path)
    steps_i = steps_i - 1



print("Paths are {}".format(','.join(database)))

innerthreshold = 3
outterthreshold = 2

##generate reading path

new_ref = []

for item in range(ref_size-steps):
    i = 0
    tmp = []
    for i in range(0,steps):
        if (get_hallname(ref[item + i]) ==  get_hallname(ref[item + i+1])):
            tmp.append(ref[item + i])
        else:
            tmp.append(ref[item + i])
            break
    if(len(tmp) == steps):
        new_ref.append(tmp)
    
new_ref = sorted(new_ref)

# for item in new_ref:
#     print(item)


# rootdir = '/Users/Qian/Desktop/wft'
# all_input = [x.strip() for x in input_open.readlines()]

# file_open = open('data_filtered.txt','r')
# all_data = [x.strip() for x in file_open.readlines()]

# path = list_files(rootdir)

cad = {}

for txtfile in database:
  input_open = open(txtfile,'r')
  all_input = [x.strip() for x in input_open.readlines()]
  

  #print(all_input)
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
    score = 0
    for path in new_ref:
        
        for txtfile in path:
            gdt = open(txtfile,'r')
            all_data = [x.strip() for x in gdt.readlines()]
            for base in all_data:
                jdata = base.split()
                jname = jdata[0]
                jvalue = float(jdata[1])
                if (iname == jname and (jvalue - innerthreshold <= ivalue and ivalue - innerthreshold <= jvalue )):
                    score +=1
            cad[path[0]] = score



max_value = max(cad.values())  # maximum value
max_keys = [k for k, v in cad.items() if v == max_value]

print(max_value, max_keys)

