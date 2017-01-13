import re
import time
import os
############## Stage 1 : removing spaces ###########
#print os.getcwd()
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"pslistinf.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"pslistinfexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()

file1=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"pslistwhi.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"pslistwhiexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()


############## Stage 2 : making excel file ##########
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"pslistinfexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("pslist")
row=0;column=0
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	sheet.write(row,column,j)
    	column+=1
    row+=1;column=0


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')


file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"pslistwhiexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("pslist")
row=0;column=0
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	sheet.write(row,column,j)
    	column+=1
    row+=1;column=0


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistwhiexcelfinal.xls')




############## Stage 3 : finding difference ###########
from xlrd import open_workbook

book1=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
first_sheet1=book1.sheet_by_index(0)
book2=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistwhiexcelfinal.xls')
first_sheet2=book2.sheet_by_index(0)

# setting up new excel sheet that consist of differences #
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("pslist_diff")
style = xlwt.easyxf('font: bold 1')
rowx=0;columnx=0
#populating heading of excel file by file2
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"pslistwhiexcel.txt","r")
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	if j=='Exit':
    		columnx+=2
    	sheet.write(rowx,columnx,j,style)
    	columnx+=1
    break
# heading written in excel file ##########################


file2.close()
#----workbook.save('pslistwhiexcelfinal.xls')
#  prior setting initalized ##############################
filetxt=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"difftxt.txt","w")
row1=2;row2=2
column=1
for row1 in range(row1,first_sheet1.nrows):
	nameofprocess1=first_sheet1.cell(row1,column).value
	#print nameofprocess1,'-----------------'
	present=0;row2=2
	for row2 in range(row2,first_sheet2.nrows):
		nameofprocess2=first_sheet2.cell(row2,column).value
		if nameofprocess2==nameofprocess1:
			present+=1
		#print nameofprocess2,present
	if present==0:
		rowx+=1;columnx=0
		for col1 in range(0,first_sheet1.ncols):
			valuetowrite=first_sheet1.cell(row1,col1).value
			sheet.write(rowx,columnx,valuetowrite)
			if columnx==2:
				filetxt.write(valuetowrite+'\n')
			columnx+=1
filetxt.close()
		#print nameofprocess1,'difference'

workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistdiff.xls')

os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcel.txt')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistwhiexcel.txt')






























	