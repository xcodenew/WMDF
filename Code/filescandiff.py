import re
import time
import os
############## Stage 1 : removing spaces ###########
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"filescaninf.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"filescaninfexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()

file1=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"filescanwhi.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"filescanwhiexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()

############## Stage 2 : making excel file ##########
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"filescaninfexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("filescan")
row=0;column=0;
for i in file2.readlines():
	
	d=i.split('|')
	
	for j in d:
		sheet.write(row,column,j)
		column+=1
	row+=1;column=0
	


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescaninfexcelfinal.xls')


file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"filescanwhiexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("filescan")
row=0;column=0;
for i in file2.readlines():
	
	
	d=i.split('|')
	
	for j in d:
		sheet.write(row,column,j)
		column+=1
	row+=1;column=0
	

file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescanwhiexcelfinal.xls')


############## Stage 3 : finding difference ###########
from xlrd import open_workbook

book1=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescaninfexcelfinal.xls')
first_sheet1=book1.sheet_by_index(0)
book2=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescanwhiexcelfinal.xls')
first_sheet2=book2.sheet_by_index(0)

# setting up new excel sheet that consist of differences #
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("filescan_diff")
style = xlwt.easyxf('font: bold 1')
rowx=0;columnx=0
#populating heading of excel file by file2
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"filescanwhiexcel.txt","r")

for i in file2.readlines():
	
	d=i.split('|')
	
	for j in d:
		#print row,column
		sheet.write(rowx,columnx,j,style)
		columnx+=1
	break
# heading written in excel file ##########################


file2.close()
#----workbook.save('filescanwhiexcelfinal.xls')
#  prior setting initalized ##############################

row1=2
rowx=0
for row1 in range(row1,first_sheet1.nrows):

	drivername1=first_sheet1.cell(row1,4).value
	access1=first_sheet1.cell(row1,3).value
	print row1,first_sheet1.nrows
	"""
	print '--------------------------1'
	print drivername1,access1
	print '--------------------------11'
	time.sleep(2)
	"""
	present=0;row2=2
	
	for row2 in range(row2,first_sheet2.nrows):
		drivername2=first_sheet2.cell(row2,4).value
		access2=first_sheet2.cell(row2,3).value
		#time.sleep(1)
		"""
		print '--------------------------2'
		print drivername2,access2
		print '-------------------------22'
		"""
		if drivername2==drivername1:
			
			
			if access2==access1:
				"""
				print 'Match Found ',drivername1,access1,drivername2,access2
				time.sleep(1)
				"""
				present+=1
				break
		
		
	if present==0:
		"""
		print 'Match not Found ',drivername1,access1,drivername2,access2
		time.sleep(0.5)
		"""
		rowx+=1;columnx=0
		for col1 in range(0,first_sheet1.ncols):
			valuetowrite=first_sheet1.cell(row1,col1).value
			sheet.write(rowx,columnx,valuetowrite)
			columnx+=1

		

workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescandiff.xls')

os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescaninfexcel.txt')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescanwhiexcel.txt')
