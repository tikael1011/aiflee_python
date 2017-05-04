'''
this script is designed to cal window algorithm
therotically, by increating size of window, finally the accuracy will be 100%
'''

'''
match a N-step sequence instead of individual points
'''


def sortlistdir(dirnamepath):
    files = glob(dirnamepath)
    a = []
    for item in range(1,len(files)+1):
    	a.append(dirnamepath[:-5] + str(item) + ".txt")
    return a

steps = int(input("Input window size: "))
innerthreshold = float(input("Input innerthreshold: "))
outterthreshold = int(input("Input outerthreshold: "))

crd = open('hallway_cod.txt','r')
crd_base = [x.strip() for x in crd.readlines()]

rootdir = '/Users/Qian/Desktop/wft'

file_open = open('data_filtered.txt','r')
all_data = [x.strip() for x in file_open.readlines()]
path = list_files(rootdir)
