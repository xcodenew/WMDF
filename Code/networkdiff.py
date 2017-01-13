import re
import time
import os
############## Stage 1 : removing spaces ###########
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"networkinf.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"networkinfexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()

file1=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"networkwhi.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"networkwhiexcel.txt","w")
for i in file1.readlines():
	d=re.sub(r' {1,}','|',i)
	file2.write(d)
file2.close()
file1.close()

############## Stage 2 : making excel file ##########
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"networkinfexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("network")
row=0;column=0;linenox=0
for i in file2.readlines():
	
	if linenox==0:
		
		i=i.replace('Local|Address','Local Address')
		
		i=i.replace('Foreign|Address','Foreign Address')
	d=i.split('|')
	if d[1]=='UDPv4' or d[1]=='UDPv6':
		d.insert(4,'N/A')
	for j in d:
		sheet.write(row,column,j)
		column+=1
	row+=1;column=0
	linenox+=1


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkinfexcelfinal.xls')


file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"networkwhiexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("network")
row=0;column=0;linenox=0
for i in file2.readlines():
	
	if linenox==0:
		
		i=i.replace('Local|Address','Local Address')
		
		i=i.replace('Foreign|Address','Foreign Address')
	d=i.split('|')
	if d[1]=='UDPv4' or d[1]=='UDPv6':
		d.insert(4,'N/A')
	for j in d:
		sheet.write(row,column,j)
		column+=1
	row+=1;column=0
	linenox+=1

file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkwhiexcelfinal.xls')




############## Stage 3 : finding difference ###########
from xlrd import open_workbook

book1=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkinfexcelfinal.xls')
first_sheet1=book1.sheet_by_index(0)
book2=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkwhiexcelfinal.xls')
first_sheet2=book2.sheet_by_index(0)

# setting up new excel sheet that consist of differences #
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("network_diff")
style = xlwt.easyxf('font: bold 1')
rowx=0;columnx=0
#populating heading of excel file by file2
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"networkwhiexcel.txt","r")
linenox=0
for i in file2.readlines():
	if linenox==0:
		
		i=i.replace('Local|Address','Local Address')
		
		i=i.replace('Foreign|Address','Foreign Address')
		
		linenox=1
	d=i.split('|')
	
	for j in d:
		#print row,column
		sheet.write(rowx,columnx,j,style)
		columnx+=1
	break
# heading written in excel file ##########################


file2.close()
#----workbook.save('networkwhiexcelfinal.xls')
#  prior setting initalized ##############################

row1=1
rowx=0
for row1 in range(row1,first_sheet1.nrows):

	ownerinf=first_sheet1.cell(row1,6).value
	localadinf=first_sheet1.cell(row1,2).value
	foreigninf=first_sheet1.cell(row1,3).value
	#checkflip=0
	present=0;row2=1
	#print ownerinf,localadinf,foreigninf,'inf1','new'
	for row2 in range(row2,first_sheet2.nrows):
		ownerwhi=first_sheet2.cell(row2,6).value
		localadwhi=first_sheet2.cell(row2,2).value
		foreignwhi=first_sheet2.cell(row2,3).value
		#time.sleep(1)
		#print ownerwhi,localadwhi,foreignwhi,'whi'
		#if ownerinf!=ownerwhi and checkflip==1:
		#	break
		if ownerinf==ownerwhi:
			#checkflip=1
			
			if localadwhi==localadinf and foreignwhi==foreigninf:
				#print 'Match Found'
				#time.sleep(2)
				present+=1
		
		
	if present==0:
		#print 'No Match'
		#time.sleep(2)
		rowx+=1;columnx=0
		for col1 in range(0,first_sheet1.ncols):
			valuetowrite=first_sheet1.cell(row1,col1).value
			sheet.write(rowx,columnx,valuetowrite)
			columnx+=1

		#print nameofprocess1,'difference'

workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkdiff.xls')

os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkinfexcel.txt')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkwhiexcel.txt')






























	