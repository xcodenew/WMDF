import re
import time
import os
import xlwt

############## Stage 1 : making excel file ###########
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"serviceinf.txt","r")
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("serviceinf")
style = xlwt.easyxf('font: bold 1')

#populating heading of excel file by file2
sheet.write(0,0,'Offset',style)
sheet.write(0,1,'Order',style)
sheet.write(0,2,'Process ID',style)
sheet.write(0,3,'Service Name',style)
sheet.write(0,4,'Display Name',style)
sheet.write(0,5,'Service Type',style)
sheet.write(0,6,'Service State',style)
sheet.write(0,7,'Binary Path',style)

row=1;column=0;linenox=0
for i in file1.readlines():
	linenox+=1
	if linenox==9:
		linenox=0
		row+=1;column=0
	else:
		i=i.split(':')
		try:
			i=i[1]
		except:
			i='   '
		
		sheet.write(row,column,i)
		
		column+=1
	
file1.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'serviceinfexcelfinal.xls')


file2=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"servicewhi.txt","r")
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("servicewhi")
style = xlwt.easyxf('font: bold 1')

#populating heading of excel file by file2
sheet.write(0,0,'Offset',style)
sheet.write(0,1,'Order',style)
sheet.write(0,2,'Process ID',style)
sheet.write(0,3,'Service Name',style)
sheet.write(0,4,'Display Name',style)
sheet.write(0,5,'Service Type',style)
sheet.write(0,6,'Service State',style)
sheet.write(0,7,'Binary Path',style)

row=1;column=0;linenox=0
for i in file2.readlines():
	linenox+=1
	if linenox==9:
		linenox=0
		row+=1;column=0
	else:
		i=i.split(':')
		try:
			i=i[1]
		except:
			i='   '
		
		sheet.write(row,column,i)
		
		column+=1
	
file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'servicewhiexcelfinal.xls')







############## Stage 2 : finding difference ###########
from xlrd import open_workbook

book1=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'serviceinfexcelfinal.xls')
first_sheet1=book1.sheet_by_index(0)
book2=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'servicewhiexcelfinal.xls')
first_sheet2=book2.sheet_by_index(0)


# setting up new excel sheet that consist of differences #
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("service_diff")
style = xlwt.easyxf('font: bold 1')

#populating heading of excel file
sheet.write(0,0,'Offset',style)
sheet.write(0,1,'Order',style)
sheet.write(0,2,'Process ID',style)
sheet.write(0,3,'Service Name',style)
sheet.write(0,4,'Display Name',style)
sheet.write(0,5,'Service Type',style)
sheet.write(0,6,'Service State',style)
sheet.write(0,7,'Binary Path',style)

# heading written in excel file ##########################

#  prior setting initalized ##############################

row1=1;rowx=0
for row1 in range(row1,first_sheet1.nrows):
	servicenameinf=first_sheet1.cell(row1,3).value
	displaynameinf=first_sheet1.cell(row1,4).value
	servicetypeinf=first_sheet1.cell(row1,5).value
	servicestateinf=first_sheet1.cell(row1,6).value
	binarypathinf=first_sheet1.cell(row1,7).value

	#checkflip=0
	present=0;row2=1
	#print ownerinf,localadinf,foreigninf,'inf1','new'
	for row2 in range(row2,first_sheet2.nrows):
		servicenamewhi=first_sheet2.cell(row2,3).value
		displaynamewhi=first_sheet2.cell(row2,4).value
		servicetypewhi=first_sheet2.cell(row2,5).value
		servicestatewhi=first_sheet2.cell(row2,6).value
		binarypathwhi=first_sheet2.cell(row2,7).value
		
		if servicenamewhi==servicenameinf:
			if displaynameinf==displaynamewhi and servicetypewhi==servicetypeinf and servicestatewhi==servicestateinf  and binarypathwhi==binarypathinf:
				present+=1;break
		
		
	if present==0:
		#print 'No Match'
		#time.sleep(2)
		rowx+=1;columnx=0
		for col1 in range(0,first_sheet1.ncols):
			valuetowrite=first_sheet1.cell(row1,col1).value
			sheet.write(rowx,columnx,valuetowrite)
			columnx+=1

		#print nameofprocess1,'difference'

workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'servicediff.xls')































	