import re
import time
import os
############## Stage 1 : removing spaces ###########
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"symlinkscaninf.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"symlinkscaninfexcel.txt","w")
counti=0
lenofcol=[]
for i in file1.readlines():
	#print '--------------'
	if counti==0:
		d=re.sub(r' {1,}','|',i)
		file2.write(d)
	elif counti==1:
		d=re.sub(r' {1,}','|',i)
		file2.write(d)
		d=d.split('|')
		for k in d:
			lenofcol.append(len(k))
	else:
		starting=0
		sentence=""
		p=[]
		countendoflist=len(lenofcol)
		countseekoflist=0
		for k in lenofcol:

			end=starting+k
			if countseekoflist==countendoflist-1:
				p.append(i[starting:])
			else:
				p.append(i[starting:end])
			starting=end+1;countseekoflist+=1
		#d=re.sub(r' {1,}','|',i)
		countendoflist=len(p)
		countseekoflist=0
		for d in p:

			if countseekoflist==countendoflist-1:
				#print 'last','-----------898989'
				sentence=sentence+d
				#print sentence
				#time.sleep(1)
			else:
				sentence=sentence+d+'|'
				#print sentence
				#time.sleep(1)
			countseekoflist+=1
		#print '1111111'
		#print sentence
		#print '2222222'
		file2.write(sentence)
	counti+=1
file2.close()
file1.close()

file1=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"symlinkscanwhi.txt","r")
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"symlinkscanwhiexcel.txt","w")
counti=0;lenofcol=[]
for i in file1.readlines():
	if counti==0:
		d=re.sub(r' {1,}','|',i)
		file2.write(d)
	elif counti==1:
		d=re.sub(r' {1,}','|',i)
		file2.write(d)
		d=d.split('|')
		for k in d:
			lenofcol.append(len(k))
	else:
		starting=0
		sentence=""
		p=[]
		countendoflist=len(lenofcol)
		countseekoflist=0
		for k in lenofcol:

			end=starting+k
			if countseekoflist==countendoflist-1:
				p.append(i[starting:])
			else:
				p.append(i[starting:end])
			starting=end+1;countseekoflist+=1
		#d=re.sub(r' {1,}','|',i)
		countendoflist=len(p)
		countseekoflist=0
		for d in p:

			if countseekoflist==countendoflist-1:
				#print 'last','-----------898989'
				sentence=sentence+d
				#print sentence
				#time.sleep(1)
			else:
				sentence=sentence+d+'|'
				#print sentence
				#time.sleep(1)
			countseekoflist+=1
		#print '1111111'
		#print sentence
		#print '2222222'
		file2.write(sentence)
	counti+=1
file2.close()
file1.close()



############## Stage 2 : making excel file ##########
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"symlinkscaninfexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("symlinkscan")
row=0;column=0;
for i in file2.readlines():
	
	d=i.split('|')
	
	for j in d:
		sheet.write(row,column,j)
		column+=1
	row+=1;column=0
	


file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscaninfexcelfinal.xls')


file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"symlinkscanwhiexcel.txt","r")
import xlwt
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("symlinkscan")
row=0;column=0;
for i in file2.readlines():
	
	
	d=i.split('|')
	
	for j in d:
		sheet.write(row,column,j)
		column+=1
	row+=1;column=0
	

file2.close()
workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscanwhiexcelfinal.xls')


############## Stage 3 : finding difference ###########
from xlrd import open_workbook

book1=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscaninfexcelfinal.xls')
first_sheet1=book1.sheet_by_index(0)
book2=open_workbook(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscanwhiexcelfinal.xls')
first_sheet2=book2.sheet_by_index(0)

# setting up new excel sheet that consist of differences #
workbook=xlwt.Workbook()
sheet=workbook.add_sheet("symlinkscan_diff")
style = xlwt.easyxf('font: bold 1')
rowx=0;columnx=0
#populating heading of excel file by file2
file2=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"symlinkscanwhiexcel.txt","r")

for i in file2.readlines():
	
	d=i.split('|')
	
	for j in d:
		#print row,column
		sheet.write(rowx,columnx,j,style)
		columnx+=1
	break
# heading written in excel file ##########################


file2.close()
#----workbook.save('symlinkscanwhiexcelfinal.xls')
#  prior setting initalized ##############################

row1=2
rowx=0
for row1 in range(row1,first_sheet1.nrows):

	file1=first_sheet1.cell(row1,5).value
	name1=first_sheet1.cell(row1,4).value
	print row1,first_sheet1.nrows
	

	#print '--------------------------1'
	#print file1,name1
	#print '--------------------------11'
	#time.sleep(2)
	
	present=0;row2=2
	
	for row2 in range(row2,first_sheet2.nrows):
		file2=first_sheet2.cell(row2,5).value
		name2=first_sheet2.cell(row2,4).value
		#time.sleep(1)
		
		#print '--------------------------2'
		#print file2,name2
		#print '-------------------------22'
		
		if file2==file1:
			
			
			if name2==name1:
				
				#print 'Match Found ',file1,name1,file2,name2
				#time.sleep(1)
				
				present+=1
				break
		
		
	if present==0:
		
		#print 'Match not Found ',file1,name1,file2,name2
		#time.sleep(0.5)
		
		rowx+=1;columnx=0
		for col1 in range(0,first_sheet1.ncols):
			valuetowrite=first_sheet1.cell(row1,col1).value
			sheet.write(rowx,columnx,valuetowrite)
			columnx+=1

		

workbook.save(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscandiff.xls')

os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscaninfexcel.txt')
os.remove(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscanwhiexcel.txt')
