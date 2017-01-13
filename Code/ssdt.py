import re
import time
import os
print 'ssdt'
file1=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"ssdtinf.txt","r")

file3=open(os.getcwd()+os.sep+"Database"+os.sep+"Analyzed_RAM_artifacts"+os.sep+"ssdtdiff.txt","w")
count=-1
for i in file1.readlines():
	#print i
	print count
	#time.sleep(2)
	count+=1
	if count<3:
		file3.write(i)
		continue
	else:
		i=i[35:]
		present=0;
		#time.sleep(2)
		#print i+'11111'
		file2=open(os.getcwd()+os.sep+"Database"+os.sep+"whitelist_artifacts"+os.sep+"ssdtwhi.txt","r")
		for j in file2.readlines():
			
			j=j[35:]

			#print j+'222222'
			if j==i:
					#time.sleep(2)
					print 'Match found',i
					#print '======'
					#print j,i
					#print '------'
					present+=1
					break
			
		file2.close()
		if present==0:
			
			print 'Match not Found ',i
			
			print 'match not found','33333'
			#time.sleep(2)
			file3.write(i)
	
	

		

file1.close()

file3.close()


