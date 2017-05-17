#utf -8
#jie qian

import random
import re
import glob
import statistics
import numpy as np
import math
import statsmodels.api as sm
import matplotlib.pyplot as plt
from math import sin
from math import cos
from time import time
 
 
 
def get_val_f(a0,a1,b1,a2,b2,a3,b3,w,x):
    wh = x * w
    return (a0 + a1 * cos(wh) + b1 * sin(wh) +
    a2 * cos(2 * wh) + b2 * sin(2 * wh) +
    a3 * cos(3 * wh) + b3 * sin(3 * wh))
 
def sortlistdir(dirnamepath):
    a = []
    files = glob.glob(dirnamepath)
    for item in files:
        temp = int(re.search(r'\d+',item).group())
        a.append(temp)
    a.sort()    
    b = []
    for item in a:
        b.append(dirnamepath[:-5] + str(item) + ".txt")
    return b
 
##REF###
# d8:84:66:4c:d1:30  ah1 mh1
# d8:84:66:4c:d1:31  ah2 mh2
# d8:84:66:4c:d1:32  ah3 mh3
# d8:84:66:4c:d1:33  ah4 mh4
# d8:84:66:4c:d1:38  ah5 mh5
# d8:84:66:4e:e7:20  ah6 mh6
# d8:84:66:4e:e7:28  ah7 mh7
# d8:84:66:4e:e7:40  ah8 mh8
# d8:84:66:4e:e7:41  ah9 mh9
# d8:84:66:4e:e7:42  ah10 mh10
# d8:84:66:4e:e7:43  ah11 mh11
# d8:84:66:4e:f0:30  ah12 mh12
# d8:84:66:4e:f0:31  ah13 mh13
# d8:84:66:4e:f0:32  ah14 mh14
# d8:84:66:4e:f0:33  ah15 mh15
# d8:84:66:4e:f0:38  ah16 mh16
# e4:f4:c6:14:ff:46  ah17 mh17
# e4:f4:c6:14:ff:47  ah18 mh18
 
###define number of pairs at certain distance####
 
 
 
 
ap_number = int(input("Input AP numbers (1~18): "))
dis_interval = float(input("Set min interval (starts 0.1): "))
test_points = int(input("Input how many points will be used for testing: "))
 
t = time ()
 
dis_list = np.arange(1,(32 + dis_interval),dis_interval)
 
 
d = [{} for i in range (1,13)]
 
h = open("apname.txt","r")
h_txt = h.read()
info = sorted(h_txt.split("\n"))
 
path = sortlistdir('/Users/Aeolus/Desktop/test/*.txt')
 
j = 0
 
method = 1
 
for txtfile in path:
    f = open(txtfile, 'r')
    #print(f)
    all_lines = f.read()
    content = sorted(all_lines.split("\n"))
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
            (d[j])[name] = real_nb
        j = j + 1
    # elif(method == 2):
    #   for name in info:
    #       nb = []
    #       for element in content:
    #           if (name == element[:17]):
    #               nb.append(int(element[-3:])) 
    #       real_nb = statistics.median(nb)
    #       (d[j])[name] = real_nb
    #   j = j + 1
 
 
#print(ap_all)
 
times = 0
error_all = []
 
for i in range(1000):
    ah1 = [-69.48,0.1092,26.77,11.52,15.86,7.718,0.934,0.1245,0]
    ah2 = [-71.18,0.3118,26.59,13.27,15.16,7.169,0.2361,0.1217,0]
    ah3 = [-61.67,3.737,15.85,4.038,10.89,3.982,3.72,0.1363,0]
    ah4 = [-65.54,1.397,21.22,7.456,14.11,6.1,2.633,0.1297,0]
    ah5 = [-59.23,6.258,11.24,0.7158,4.315,-1.451,0.6008,0.1582,0]
    ah6 = [-73.73,-9.976,-3.47,2.457,-0.4293,-1.54,-0.4905,0.2088,0]
    ah7 = [-63.39,-9.389,-5.342,1.243,0.9042,-0.3874,-2.647,0.2252,0]
    ah8 = [-54.51,-9.72,-6.966,-2.343,4.908,2.103,0.1965,0.1467,0]
    ah9 = [-56.11,-10.38,-4.424,-1.437,5.532,2.315,0.5102,0.1452,0]
    ah10 = [-55.14,-10.97,-5.733,-1.585,6.02,2.314,0.3298,0.1443,0]
    ah11 = [-55.54,-11.51,-5.127,-1.336,6.378,2.392,0.2452,0.1434,0]
    ah12 = [-72.16,-10.69,11.81,2.766,0.2359,1.291,1.425,0.1401,0]
    ah13 = [-71.21,-11.55,9.719,2.414,0.5842,0.6808,1.757,0.1465,0]
    ah14 = [-75.44,-11.09,17.42,3.746,1.591,3.176,1.071,0.1309,0]
    ah15 = [-73.6,-11.03,14.34,3.071,1.099,2.118,1.458,0.1359,0]
    ah16 = [-62.43,-10.99,7.384,0.8127,2.242,-1.001,-1.259,0.1882,0]
    ah17 = [-70.32,-13.34,-8.058,-0.5656,-0.8235,2.392,3.586,0.158,0]
    ah18 = [-56.33,-9.875,-6.821,1.236,1.945,0.01161,-0.8559,0.2267,0]
    ###remeber to replace xx[-1] to the actual 'x' value
 
    ah = [ah1,ah2,ah3,ah4,ah5,ah6,ah7,ah8,ah9,ah10,
    ah11,ah12,ah13,ah14,ah15,ah16,ah17,ah18]
 
    ap_all = [ [] for i in range (1,19)]
 
    for item in d:
        k = 0
        for key, val in sorted(item.items()):
            ap_all[k].append(val)
            k = k + 1
 
 
    weight = random.randint(0,(12 - test_points))
    ###get the 'proper length of test points'###
    for i in range(18):
        ap_all[i] = ap_all[i][weight:(weight + test_points)]
 
    ref = random.sample(range(18),ap_number)
 
    #print(ref)
 
    pos_can = [[] for i in range(test_points)]
 
    for i in dis_list:
        for k in ref:
            l = 0
            ah[k][-1] = i
            tmp = get_val_f(*ah[k])
            for test_data in ap_all[k]:
                if (math.fabs(tmp - test_data) <= 2):
                    #print(pos_can[l])
                    #print(l)
                    pos_can[l].append(i)
                l = l + 1
 
    for i in range(test_points):
        if (pos_can[i] == []):
            pos_can[i] = [0]
 
 
    start = math.fabs((weight + 18)/4 - statistics.median(pos_can[0]))
    end = math.fabs((weight + 18 + test_points)/4 - statistics.median(pos_can[-1]))
    # print("The ground truth is {} to {}".format((weight + 18)/4,(weight + 
    #   18 + test_points)/4))
    # print("error at start is {} and error at end is {}".format(start,end))
 
    error = (start + end) / 2
    error_all.append(error)
#print(error)
 
 
print(max(error_all))
print(min(error_all))
print(statistics.median(error_all))
print("Takes time: {}s".format(time()-t))
 
 
'''
WITH threshold = 2
#Interval Test
 
testing_1 10,0.1,6
result: 3.25,0.05,1.35
 
testing_2 10,0.3,6
result: 3.6,0.075,1.35
 
testing_3 10,0.5,6
result: 3.25,0,1.25
 
testing_4 10,1,6
result: 3.5,0,1.25
 
testing_5 10,2,6
result: 10,0.25,1.25
 
---> interval choose 0.5
'''
'''
WITH threshold = 2
#AP Test
 
testing_1 2,0.5,6
result: 18.5,0,1.5
 
testing_2 4,0.5,6
result: 17.25,0,1.375
 
testing_3 6,0.5,6
result: 12.5(varies a lot),0,1.25
 
testing_4 8,0.5,6
result: 4,0,1.25
 
testing_5 12,0.5,6
result: 3,0,1.25
 
testing_6 14,0.5,6
result: 2.7,0,1.25
 
testing_7 16,0.5,6
result: 2.5,0,1.125
 
testing_8 18,0.5,6
result: 1.75,0.375,1.125
 
---> AP number choose 18
'''
'''
WITH threshold = 2
#Distance Test
 
testing_1 18,0.5,2
result: 2,0.625,1.125
 
testing_2 18,0.5,4
result: 1.75,0.625,1.125
 
testing_3 18,0.5,8
result: 1.5,0.75,1.5
 
testing_4 18,0.5,10
result: 1.75,0.625,1.5
 
testing_5 18,0.5,12
result: 1.25,1.25,1.25
 
testing_6 18,0.5,1
result:  3.625,0.125,1.375
 
 
---> Distance choose 6
'''
 
 
###plot 18,0.5,6
 
ecdf = sm.distributions.ECDF(error_all)
 
x = np.linspace(min(error_all), max(error_all))
y = ecdf(x)
plt.step(x, y)
plt.show()
 
 
#random.shuffle(ah)
# del ah[0][-1]
