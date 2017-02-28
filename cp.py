import glob
import xlsxwriter
import re


workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column(1, 1, 15)
worksheet.set_column(3, 1, 15)
worksheet.write('A1', 'No')
worksheet.write('B1', 'Ap Name')
worksheet.write('C1', 'Freq')
worksheet.write('D1', 'Time Stamp')
worksheet.write('E1', 'Strength')

row = 1
col = 1
point = 1


def sortlistdir(dirnamepath):
	files = glob.glob(dirnamepath)	
	a = []
	for item in range(1,len(files)+1):
		a.append(dirnamepath[:-5] + str(item) + ".txt")
	#print(a)
	return a


path = sortlistdir('/Users/Qian/Desktop/wifidata/V_Four/*.txt')

for txtfile in path:
	h = open(txtfile,'r')
	h_txt = h.read()
	info = sorted(h_txt.split("\n"))
	#g = open(txtfile,'w')
	worksheet.write(row,1,point)
	for line in info:
		if(line == ''): continue
		if(line != '****####****'):
			item = line.split()
			if (len(item) != 4):
				print (txtfile)
				
			worksheet.write(row,0,point)
			worksheet.write_string(row,col,item[0])
			worksheet.write_number(row,col+1,int(item[1]))
			worksheet.write_number(row,col+2,int(item[2]))
			worksheet.write_number(row,col+3,int(item[3]))
			row = row + 1
	h.close()
	point  = point + 1

workbook.close()
print("done!")
