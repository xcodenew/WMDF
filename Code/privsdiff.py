import re
import time
import os
############## Stage 1 : removing spaces ###########
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"privsinf.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"privsinfexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()

file1=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"privswhi.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"privswhiexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()

############## Stage 2 : making excel file ##########
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"privsinfexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("privs")
row=0;column=0
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	sheet.write(row,column,j)
    	column+=1
    row+=1;column=0


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privsinfexcelfinal.xls')


file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"privswhiexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("privs")
row=0;column=0
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	sheet.write(row,column,j)
    	column+=1
    row+=1;column=0


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privswhiexcelfinal.xls')



############## Stage 3 : finding difference ###########
from xlrd import open_workbook

book1=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privsinfexcelfinal.xls')
first_sheet1=book1.sheet_by_index(0)
book2=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privswhiexcelfinal.xls')
first_sheet2=book2.sheet_by_index(0)

# setting up new excel sheet that consist of differences #
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("privs_diff")
style = xlwt.easyxf('font: bold 1')
rowx=0;columnx=0
#populating heading of excel file by file2
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"privswhiexcel.txt","r")
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	if j=='Exit':
    		columnx+=2
    	sheet.write(rowx,columnx,j,style)
    	columnx+=1
    break
file2.close()
# heading written in excel file ##########################


#  prior setting initalized ##############################

row1=2
rowx=0
for row1 in range(row1,first_sheet1.nrows):
	row2=2
	privilege1=first_sheet1.cell(row1,5).value
	if privilege1=='Present,Enabled':
		skipprivilege=0
		pidofthatprocess=first_sheet1.cell(row1,2).value
		attributeofthatprocess=first_sheet1.cell(row1,4).value
		checkflip=0
		for row2 in range(row2,first_sheet2.nrows):
			pidofthisprocess=first_sheet2.cell(row2,2).value
			attributeofthisprocess=first_sheet2.cell(row2,4).value
			if pidofthatprocess!=pidofthisprocess and checkflip==1:
				break
			if pidofthatprocess==pidofthisprocess:
				checkflip=1
				if attributeofthisprocess==attributeofthatprocess:
					 privilege2=first_sheet2.cell(row1,5).value
					 if privilege2=='Present,Enabled':
					 	skipprivilege=1
		if skipprivilege==0:
			rowx+=1;columnx=0
			for colx in range(0,first_sheet1.ncols):
				valuetowritex=first_sheet1.cell(row1,colx).value
				#print '======',valuetowritex,'------',len(valuetowritex),'+++'
				if len(valuetowritex)>0:
					sheet.write(rowx,columnx,valuetowritex)
					columnx+=1
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privsdiff.xls')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privsinfexcel.txt')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privswhiexcel.txt')











	