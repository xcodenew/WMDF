import re
import time
import os
import xlwt

file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"malfindinf.txt","r")

file3=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"malfinddiff.txt","w")

def checkmatch(textproc1):

	file2=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"malfindwhi.txt","r")
	textinf=[];countblank=0;firstline=0
	for i in file2.readlines():
		textproc2=[]
		if firstline==0:
			myfirstline=i
			myfirstline=myfirstline.split(' ')


			firstline=1
		if len(i)==1:
			countblank+=1
		else:
			textinf.append(i)

		if countblank==3:
			firstline=0
			countblank=0
			line1=textinf[3]
			line1=line1.split('  ')
			textproc2.append(line1[1])
			
			line1=textinf[4]
			line1=line1.split('  ')
			textproc2.append(line1[1])
			
			line1=textinf[5]
			line1=line1.split('  ')
			textproc2.append(line1[1])
			
			line1=textinf[6]
			line1=line1.split('  ')
			textproc2.append(line1[1])
			
			textproc2.append(myfirstline[1])
			"""
			print '+++++++++++++++++-------------+++++++++++'
			print textproc2
			print '-----------------+++++++++++++-----------'
			"""
			if textproc1==textproc2:
				#print 'Match Found'
				#time.sleep(3)
				return True
	else:
		return False			
	file2.close()

## original  function code ########################
textinf=[];countblank=0;firstline=0;totalstring=""
for i in file1.readlines():
	totalstring=totalstring+i
	textproc1=[]
	if firstline==0:
		myfirstline=i
		myfirstline=myfirstline.split(' ')


		firstline=1
	if len(i)==1:
		countblank+=1
	else:
		textinf.append(i)

	if countblank==3:
		firstline=0
		countblank=0
		line1=textinf[3]
		line1=line1.split('  ')
		textproc1.append(line1[1])
		
		line1=textinf[4]
		line1=line1.split('  ')
		textproc1.append(line1[1])
		
		line1=textinf[5]
		line1=line1.split('  ')
		textproc1.append(line1[1])
		
		line1=textinf[6]
		line1=line1.split('  ')
		textproc1.append(line1[1])
		
		textproc1.append(myfirstline[1])
		"""
		print '===============----------==========='
		print textproc1
		#time.sleep(2)
		print '---------------==========-----------'
		"""
		resultofmatch=checkmatch(textproc1)
		if resultofmatch!=True:
			file3.write(totalstring)
			"""
			print '-----------------------------++++'
			print totalstring
			print '++++-----------------------------'
			print 'No Match Found'
			"""
			#time.sleep(2)

		totalstring=""

		

file1.close()

file3.close()
































	