import re
import time
import os
############## Stage 1 : removing spaces ###########
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"driverscaninf.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"driverscaninfexcel.txt","w")
for i in file1.readlines():
	firstcol=i[0:18].replace(' ','');secondcol=i[19:23].replace(' ','');thirdcol=i[24:28].replace(' ','')
	fourthcol=i[29:46].replace(' ','');fifthcol=i[47:66].replace(' ','');sixthcol=i[66:85].replace(' ','')
	seventhcol=i[87:98].replace(' ','');eightcol=i[100:].replace(' ','')
	if len(firstcol)==0:
		firstcol='BLANK'
	if len(secondcol)==0:
		secondcol='BLANK'
	if len(thirdcol)==0:
		thirdcol='BLANK'
	if len(fourthcol)==0:
		fourthcol='BLANK'
	if len(fifthcol)==0:
		fifthcol='BLANK'
	if len(sixthcol)==0:
		sixthcol='BLANK'
	if len(seventhcol)==0:
		seventhcol='BLANK'
	if len(eightcol)==0:
		eightcol='BLANK\n'
	i=firstcol+'|'+secondcol+'|'+thirdcol+'|'+fourthcol+'|'+fifthcol+'|'+sixthcol+'|'+seventhcol+'|'+eightcol
	file2.write(i)
file2.close()
file1.close()

file1=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"driverscanwhi.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"driverscanwhiexcel.txt","w")
for i in file1.readlines():
	firstcol=i[0:18].replace(' ','');secondcol=i[19:23].replace(' ','');thirdcol=i[24:28].replace(' ','')
	fourthcol=i[29:46].replace(' ','');fifthcol=i[47:66].replace(' ','');sixthcol=i[66:85].replace(' ','')
	seventhcol=i[87:98].replace(' ','');eightcol=i[100:].replace(' ','')
	if len(firstcol)==0:
		firstcol='BLANK'
	if len(secondcol)==0:
		secondcol='BLANK'
	if len(thirdcol)==0:
		thirdcol='BLANK'
	if len(fourthcol)==0:
		fourthcol='BLANK'
	if len(fifthcol)==0:
		fifthcol='BLANK'
	if len(sixthcol)==0:
		sixthcol='BLANK'
	if len(seventhcol)==0:
		seventhcol='BLANK'
	if len(eightcol)==0:
		eightcol='BLANK\n'
	i=firstcol+'|'+secondcol+'|'+thirdcol+'|'+fourthcol+'|'+fifthcol+'|'+sixthcol+'|'+seventhcol+'|'+eightcol
	file2.write(i)
file2.close()
file1.close()

############## Stage 2 : making excel file ##########
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"driverscaninfexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("driverscan")
row=0;column=0
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	sheet.write(row,column,j)
    	column+=1
    row+=1;column=0


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscaninfexcelfinal.xls')


file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"driverscanwhiexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("driverscan")
row=0;column=0
for i in file2.readlines():
    d=i.split('|')
    for j in d:
    	#print row,column
    	sheet.write(row,column,j)
    	column+=1
    row+=1;column=0


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscanwhiexcelfinal.xls')



############## Stage 3 : finding difference ###########
from xlrd import open_workbook

book1=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscaninfexcelfinal.xls')
first_sheet1=book1.sheet_by_index(0)
book2=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscanwhiexcelfinal.xls')
first_sheet2=book2.sheet_by_index(0)

# setting up new excel sheet that consist of differences #
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("driverscan_diff")
style = xlwt.easyxf('font: bold 1')
rowx=0;columnx=0
#populating heading of excel file by file2
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"driverscanwhiexcel.txt","r")
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
	drivername1=first_sheet1.cell(row1,7).value
	name1=first_sheet1.cell(row1,6).value
	servicekey1=first_sheet1.cell(row1,5).value
	"""
	print drivername1,name1,servicekey1,'111111'
	time.sleep(2)
	"""
	nomatch=0
	checkflip=0
	for row2 in range(row2,first_sheet2.nrows):
		drivername2=first_sheet2.cell(row2,7).value
		name2=first_sheet2.cell(row2,6).value
		servicekey2=first_sheet2.cell(row2,5).value
		"""
		print '-------'
		print drivername2,name2,servicekey2,'222222'
		time.sleep(1)
		print '======='
		"""
		if drivername1!=drivername2 and checkflip==1:
			"""
			print 'breaking inner loop'
			time.sleep(1)
			"""
			break
		if drivername2==drivername1 and name2==name1 and servicekey2==servicekey1:
			"""
			print 'match found'
			time.sleep(1)
			"""
			checkflip=1
			nomatch=1
	if nomatch==0:
		rowx+=1;columnx=0
		for colx in range(0,first_sheet1.ncols):
			valuetowritex=first_sheet1.cell(row1,colx).value
			#print '======',valuetowritex,'------',len(valuetowritex),'+++'
			if len(valuetowritex)>0:
				sheet.write(rowx,columnx,valuetowritex)
				columnx+=1
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driversdiff.xls')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscaninfexcel.txt')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscanwhiexcel.txt')











	