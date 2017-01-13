import Tkinter, Tkconstants, tkFileDialog
from Tkinter import Tk, BOTH,StringVar
#from ttk import Frame, Button, Style , Label,Entry,Menu
from ttk import Style
from Tkinter import *
import urllib
import tkMessageBox
import os
import os.path
import sys
from PIL import Image,ImageTk
aaa=8
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.v = StringVar()
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = parent
        options['title'] = 'This is a title'

        self.initUI()

    def updatelabel1(self,textt):
        totaltext=self.v.get()
        totaltext=totaltext.split('\n')
        #print len(totaltext)
        
        if len(totaltext)>26:
            self.v.set('Status: ')
        
        self.v.set(self.v.get()+"\n"+textt)

    def seldll(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected')
            return 1
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted Dll info for selected')
        self.updatelabel1('process that are different..')
        try:
            
            filetxt=open(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'difftxt.txt',"r")
            processlist=''
            for tt in filetxt.readlines():
                processlist=processlist+tt.strip()+','
            filetxt.close()
            ttlen=len(processlist)
            processlist=processlist[0:ttlen-1]
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'selected_dlllist.txt'):
                pass
            else:
                self.updatelabel1('Dlllist artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' dlllist -p '+processlist+' > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'selected_dlllist.txt')
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' ldrmodules -p '+processlist+' > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'selected_hidden_dlllist.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            #os.system(os.getcwd()+os.sep+'Database'+os.sep+'pslistdiff.exe')
            #self.updatelabel1('Analyzed difference :: pslist')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'selected_dlllist.txt')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'selected_hidden_dlllist.txt')
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing extracting DLLlist.')

    def selhandles(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted handles info for selected')
        self.updatelabel1('process that are different..')
        try:
            
            filetxt=open(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'difftxt.txt',"r")
            processlist=''
            for tt in filetxt.readlines():
                processlist=processlist+tt.strip()+','
            filetxt.close()
            ttlen=len(processlist)
            processlist=processlist[0:ttlen-1]
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'selected_handles.txt'):
                pass
            else:
                self.updatelabel1('Selected Handles artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' handles -p '+processlist+' > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'selected_handles.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            #os.system(os.getcwd()+os.sep+'Database'+os.sep+'pslistdiff.exe')
            #self.updatelabel1('Analyzed difference :: pslist')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'selected_handles.txt')
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing extracting DLLlist.')

    def handles(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        print 'handles on way..'
        self.updatelabel1('handles')

    def willcome(self):
        tkMessageBox.showinfo("Updater Message", "This feature will be active in next version")
        
    def pslist(self):
        ## need to modify
        """
        if len(self.filename)<1:
            self.updatelabel1('! Suspicious artifacts not selected.')
            return 1
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted Pslist info from Image..')
        """
        ###
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinf.txt'):
                pass
            else:
                ##os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' pslist > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'pslistinf.txt')
                self.updatelabel1('Pslist artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'pslistdiff.exe')
            self.updatelabel1('Analyzed difference :: pslist')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename


    def psscan(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        print 'psscan on way..'
        self.updatelabel1('psscan')

    def pstree(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted pstree info from Image..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pstreeinf.txt'):
                pass
            else:
                self.updatelabel1('Pstree artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' pstree > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'pstreeinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            #os.system(os.getcwd()+os.sep+'Database'+os.sep+'pslistdiff.exe')
            #self.updatelabel1('Analyzed difference ::')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pstreeinf.txt')
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
    def psxview(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted psxview info from Image..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'psxviewinf.txt'):
                pass
            else:
                self.updatelabel1('Psxview artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' psxview > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'psxviewinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            #os.system(os.getcwd()+os.sep+'Database'+os.sep+'pslistdiff.exe')
            #self.updatelabel1('Analyzed difference ::')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'psxviewinf.txt')
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
    def psscan_dot(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted psscan_dot info from Image..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'psscan_dot.dot'):
                pass
            else:
                self.updatelabel1('Psscan_dot artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' psscan --output=dot --output-file='+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'psscan_dot.dot')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            #os.system(os.getcwd()+os.sep+'Database'+os.sep+'pslistdiff.exe')
            #self.updatelabel1('Analyzed difference ::')
            tkMessageBox.showinfo("Updater Message", "The graphic dot file is created under database directory. You can view it using open-source Graphviz Software.")
            self.updatelabel1('The graphic dot file ')
            self.updatelabel1('created under database directory')
            self.updatelabel1('You can view it using')
            self.updatelabel1('open-source Graphviz Software.')
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pstreeinf.txt')
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
    def services(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted services info from Image..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'serviceinf.txt'):
                pass
            else:
                self.updatelabel1('services artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' svcscan > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'serviceinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'servicediff.exe')
            self.updatelabel1('Analyzed difference :: services')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'serviceinfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'servicediff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
    def malfind(self):
        #print 'in malfind'
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted malfind info from Image..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'malfindinf.txt'):
                pass
            else:
                self.updatelabel1('malfind artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' malfind > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'malfindinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'malfinddiff.exe')
            self.updatelabel1('Analyzed difference :: malfind')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'malfindinf.txt')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'malfinddiff.txt')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
    def mftparser(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'mftparser on way..'
        self.updatelabel1('Mft Parsed Successfully')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'mftparserinf.txt'):
                pass
            else:
                self.updatelabel1('mftparserinf artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' mftparser -C --output=body --output-file='+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'mftparserinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
    def netscan(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted network connections info from Image..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkinf.txt'):
                pass
            else:
                self.updatelabel1('netscan artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' netscan > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'networkinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'networkdiff.exe')
            self.updatelabel1('Analyzed difference :: network')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkinfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'networkdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
    def privs(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted privillege  info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privsinf.txt'):
                pass
            else:
                self.updatelabel1('Privs artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' privs > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'privsinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'privsdiff.exe')
            self.updatelabel1('Analyzed difference :: privillege')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privsinfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'privsdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
    def driverscan(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted driverscan info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscaninf.txt'):
                pass
            else:
                self.updatelabel1('Driverscan artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' driverscan > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'driverscaninf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'driverscandiff.exe')
            self.updatelabel1('Analyzed difference :: driverscan')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driverscaninfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'driversdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
        #self.updatelabel1('driverscan')
    def filescan(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted filescan info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescaninf.txt'):
                pass
            else:
                self.updatelabel1('Filescan artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' filescan > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'filescaninf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'filescandiff.exe')
            self.updatelabel1('Analyzed difference :: filescan')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescaninfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'filescandiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
        #self.updatelabel1('driverscan')
    def modscan(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted modscan info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'modscaninf.txt'):
                pass
            else:
                self.updatelabel1('modscan artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' modscan > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'modscaninf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'modscandiff.exe')
            self.updatelabel1('Analyzed difference :: modscan')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'modscaninfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'modscandiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
        #self.updatelabel1('driverscan')
    def modules(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted modules info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'modules.txt'):
                pass
            else:
                self.updatelabel1('Modules artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' modules > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'modules.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'modules.exe')
            self.updatelabel1('Analyzed difference :: modules')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'modulesinfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'modulesdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
        #self.updatelabel1('driverscan')
    def ssdt(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted ssdt info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'ssdtinf.txt'):
                pass
            else:
                self.updatelabel1('Ssdt artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' ssdt > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'ssdt.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'ssdt.exe')
            self.updatelabel1('Analyzed difference :: ssdt')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'ssdtinf.txt')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'ssdtdiff.txt')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
        #self.updatelabel1('driverscan')
    def symlinkscan(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted symlinkscan info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscaninf.txt'):
                pass
            else:
                self.updatelabel1('Symlinkscan artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' symlinkscan > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'symlinkscaninf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'symlinkscan.exe')
            self.updatelabel1('Analyzed difference :: symlinkscan')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscaninfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'symlinkscandiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
        #self.updatelabel1('driverscan')
    def unloadedmodules(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        #print 'in malfind'
        self.profilename=self.entry1.get()
        self.updatelabel1('Extracted unloadedmodules info ..')
        try:
            if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'unloadedmodulesinf.txt'):
                pass
            else:
                self.updatelabel1('unloadedmodulesinf artifacts from ')
                self.updatelabel1('suspicious system not found...')
                return 1
                #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' unloadedmodules > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'unloadedmodulesinf.txt')
        except Exception as ex:
            self.updatelabel1(ex)
        try:
            #print os.getcwd()
            #os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'pslistinfexcelfinal.xls')
            #self.updatelabel1('Analyzing difference ::')
            os.system(os.getcwd()+os.sep+'Database'+os.sep+'unloadedmodules.exe')
            self.updatelabel1('Analyzed difference :: unloadedmodules')
            
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'unloadedmodulesinfexcelfinal.xls')
            os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'unloadedmodulesdiff.xls')
        except:
            self.updatelabel1('!Error while analyzing difference.')
        #print self.filename
        #self.updatelabel1('pstree')
        #self.updatelabel1('driverscan')
    
    def menu11(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'alldlllistinf.txt'):
                pass
        else:
            self.profilename=self.entry1.get()
            #print 'Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' dlllist > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'alldlllistinf.txt'
            #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' dlllist > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'alldlllistinf.txt')
        os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'alldlllistinf.txt')
        pass
    def menu12(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'allhandlesinf.txt'):
                pass
        else:
            self.profilename=self.entry1.get()
            #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' handles > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'allhandlesinf.txt')
        os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'allhandlesinf.txt')
        pass
    def menu13(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'allcallbacksinf.txt'):
                pass
        else:
            self.profilename=self.entry1.get()
            #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' callbacks > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'allcallbacksinf.txt')
        os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'allcallbacksinf.txt')
        pass
    def menu14(self):
        if len(self.filename)<1:
            self.updatelabel1('Suspicious artifacts not selected.')
            return 1
        if os.path.exists(os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'alltimersinf.txt'):
                pass
        else:
            self.profilename=self.entry1.get()
            #os.system('Volatility'+os.sep+'volatility-2.3.1.standalone.exe  -f '+self.filename+' --profile='+self.profilename+' timers > '+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'alltimersinf.txt')
        os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"Analyzed_RAM_artifacts"+os.sep+'alltimersinf.txt')
        pass
    def menu21(self):
        #tkMessageBox.showinfo("Important Information", "Please note this plugins needs Python installed and installation will be initiated for first use")
        tkMessageBox.showinfo("Updater Message", "This feature will be active in next version")
        pass
    def menu22(self):
        #tkMessageBox.showinfo("Important Information", "Please note this plugins needs Python installed and installation will be initiated for first use")
        tkMessageBox.showinfo("Updater Message", "This feature will be active in next version")
        pass
    def updateme(self):
        tkMessageBox.iconbitmap(default='favicon.ico')
        tkMessageBox.showinfo("Updater Message", "A new update is available. If you are an authorized user: \nPlease map network drive to IP : \\10.12.67.240\share$ . You can get the latest version under folder X-Labs , copy the whole folder named WMDF")
        pass
    def helpme(self):
        os.system('start '+os.getcwd()+os.sep+'Database'+os.sep+"docs"+os.sep+'WMDF.pdf')
    

    def askopenfilename1(self):
        #useless code will remove after sometime
        #self.filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.filename='Not Applicable'
        
        ###################
        tkMessageBox.showinfo("Important Information", "Please note the filename format of suspicious artifacts should be suffixed with inf , For ex: pslistinf.txt")
        
        self.foldername1 = tkFileDialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        #self.filename='Not Applicable'
        print self.foldername1

        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(self.foldername1) if isfile(join(self.foldername1, f))]
        self.foldername1=self.foldername1.replace("/",os.sep)
        for ik in onlyfiles:
            
            nameoffile=self.foldername1+os.sep+ik
            #nameoffile=nameoffile.replace(r'\\','/')
            try:
                #print 'copy '+nameoffile+' '+os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+ik
                os.system('copy '+nameoffile+' '+os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+ik)
            except:
                pass


        #self.updatelabel1(self.foldername1)
        self.updatelabel1('Loaded-Suspicious artifacts')
        tkMessageBox.showinfo("Important Information", "Always use the updated version. If you are an authorized user: \nPlease map network drive to IP : \\10.12.67.240\share$ . You can get the latest version under folder X-Labs , copy the whole folder named WMDF")
        
    def askopenfilename2(self):
        #useless code will remove after sometime
        #self.filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.filename='Not Applicable'
        
        ###################
        
        self.foldername2 = tkFileDialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        #self.filename='Not Applicable'
        print self.foldername2

        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(self.foldername2) if isfile(join(self.foldername2, f))]
        self.foldername2=self.foldername2.replace("/",os.sep)
        for ik in onlyfiles:
            nameoffile=self.foldername2+os.sep+ik
            try:
                #print 'copy '+nameoffile+' '+os.getcwd()+os.sep+'Database'+os.sep+'whitelist_artifacts'+os.sep+ik
                os.system('copy '+nameoffile+' '+os.getcwd()+os.sep+'Database'+os.sep+'whitelist_artifacts'+os.sep+ik)
            except:
                pass






        self.updatelabel1('Loaded-Whitelist artifacts')
        self.updatelabel1('Loaded..')
        tkMessageBox.showinfo("Important Information", "Always use the updated version. If you are an authorized user: \nPlease map network drive to IP : \\10.12.67.240\share$ . You can get the latest version under folder X-Labs , copy the whole folder named WMDF")
        

    def hello(self):
        print ""
    
    def initUI(self):
      
        self.parent.title("Windows MemDiff Forensics Tool")
        self.style = Style()
        self.style.theme_use("default")
        self.filename=''
        self.profilename=''
        self.entry1=''
        self.pack(fill=BOTH, expand=1)
        askfilenamebutton1=Button(self, text="Select Suspicious artifacts",
            command=self.askopenfilename1)
        askfilenamebutton2=Button(self, text="Select Whitelist artifacts",
            command=self.askopenfilename2)
        updatelabel1button=Button(self, text="update label",
            command=self.updatelabel1)
        
        
        self.v.set('Status: ')

        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu1 = Menu(menubar)
        fileMenu2 = Menu(menubar)
        """
        fileMenu2.add_command(label="Look for IOC", command=self.menu21)
        fileMenu2.add_command(label="Execute Autorun Plugin", command=self.menu22)
        fileMenu.add_command(label="All process dlls", command=self.menu11)

        fileMenu.add_command(label="All process  Handles", command=self.menu12)

        fileMenu.add_command(label="Look for callbacks", command=self.menu13)
        fileMenu.add_command(label="Look for timers", command=self.menu14)
        fileMenu.add_command(label="Exit", command=self.quit)
        fileMenu1.add_command(label="Specific Dll", command=self.willcome)
        fileMenu1.add_command(label="Specific Process", command=self.willcome)
        

        menubar.add_cascade(label="Execute Volatility Modules", menu=fileMenu)
        menubar.add_cascade(label="Extract Dll,Process", menu=fileMenu1)
        menubar.add_cascade(label="New Volatility Plugins", menu=fileMenu2)
        """
        #img = ImageTk.PhotoImage(Image.open('favicon.ico'))
        #img_label = Label(self, image=img)
        #img_label.pack()
        
        labelupdate=Label(self, textvariable=self.v)
        labelupdate.config(background='green')
        #v.set("New Text!")

        quitButton = Button(self, text="     Quit       ",
            command=self.quit)
        helpButton = Button(self, text="     HELP      ",
            command=self.helpme)

        #updatewhite=Button(self,text="Update whitelist artifacts ",command=self.updateme,fg='blue')
        askfilenamebutton1.place(x=50,y=10)
        askfilenamebutton2.place(x=50,y=40)
        #labeljunk=Label(self, text='enter Profile: ')
        #labeljunk.place(x=50,y=55)
        self.entry1=Entry(self)
        self.entry1.insert(0, "Win7SP1x64")
        
        labelupdate.place(x=50,y=110)
        #updatelabel1button.place(x=50,y=300)
        quitButton.place(x=50, y=700)
        helpButton.place(x=140,y=700)
        """
        try:
            ww=urllib.urlopen('http://lalughantal.site90.com/updatevola.html')
            if ww.read()=='<html>\n<body>\n1\n</body></html>\r\n<!-- Hosting24 Analytics Code -->\r\n<script type="text/javascript" src="http://stats.hosting24.com/count.php"></script>\r\n<!-- End Of Analytics Code -->\r\n':
                
                updatewhite.place(x=50,y=740)
        except Exception as ex:
            print ex
            pass
        """

        ######
        labelprocess=Label(self, text='Compare Process -----------------',fg='red')
        labelprocess.place(x=300,y=10)

        pslist=Button(self, text="Compare Pslist",
            command=self.pslist)
        pslist.place(x=300,y=40)



        psscan=Button(self, text="Compare psxview",
            command=self.psxview)
        psscan.place(x=420,y=40)

        pstree=Button(self, text="Compare pstree",
            command=self.pstree)
        pstree.place(x=300,y=80)

        psscan_dot=Button(self, text="Compare psscan_dot",
            command=self.psscan_dot)
        psscan_dot.place(x=420,y=80)

        #psxview=Button(self, text="Compare psxview",command=self.psxview)
        #psxview.place(x=300,y=120)

        labelservices=Label(self, text='Compare Services --------------------',fg='red')
        labelservices.place(x=300,y=130)
        

        services=Button(self, text="Compare services",
            command=self.services)
        services.place(x=300,y=160)

        labelcodeinj=Label(self, text='Compare Code Injection ------------------',fg='red')
        labelcodeinj.place(x=300,y=200)

        malfind=Button(self, text="Compare malfind",
            command=self.malfind)
        malfind.place(x=300,y=230)

        labelmft=Label(self, text='Compare File Present -------------------',fg='red')
        labelmft.place(x=300,y=270)

        mftparser=Button(self, text="Compare mftparser",
            command=self.mftparser)
        mftparser.place(x=300,y=300)

        labelnet=Label(self, text='Compare Network Connections ----------------',fg='red')
        labelnet.place(x=300,y=340)

        netscan=Button(self, text="Compare netscan",
            command=self.netscan)
        netscan.place(x=300,y=370)

        labelpriv=Label(self, text='Compare Privillege -------------------',fg='red')
        labelpriv.place(x=300,y=410)

        privs=Button(self, text="Compare privs",
            command=self.privs)
        privs.place(x=300,y=440)


        labelxtra=Label(self, text='Compare selected Dll,Handles --------------------',fg='red')
        labelxtra.place(x=300,y=490)

        dll=Button(self, text="Compare dll",
            command=self.seldll)
        dll.place(x=300,y=520)

        handles=Button(self, text="Compare handles",
            command=self.selhandles)
        handles.place(x=400,y=520)

        labelxtra=Label(self, text='Compare Kernel modules--------------------',fg='red')
        labelxtra.place(x=300,y=560)

        driverscan=Button(self, text="Compare driverscan",
            command=self.driverscan)
        driverscan.place(x=300,y=590)

        filescan=Button(self, text="Compare filescan",
            command=self.filescan)
        filescan.place(x=440,y=590)

        modscan=Button(self, text="Compare modscan",
            command=self.modscan)
        modscan.place(x=300,y=630)

        modules=Button(self, text="Compare modules",
            command=self.modules)
        modules.place(x=440,y=630) 
        """
        im=Image.open('favicon.ico')
        tkimage=ImageTk.PhotoImage(im)
        background_label = Label(image=im)
        background_label.image=im
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        """
        symlinkscan=Button(self, text="Compare symlinkscan",
            command=self.symlinkscan)
        symlinkscan.place(x=300,y=670) 

        unloadedmodules=Button(self, text="Compare unloadedmodules",
            command=self.unloadedmodules)
        unloadedmodules.place(x=460,y=670) 

        ssdt=Button(self, text="Compare ssdt",
            command=self.ssdt)
        ssdt.place(x=300,y=710)


        ######



def mainc():
    
    ###################
    """
    from Tkinter import *
    import tkMessageBox
    import Tkinter
    #jok=open("checkme.txt","w")
    

    top = Tkinter.Tk()
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    cc1 = Checkbutton(top, text = "Compare Artifacts", variable = CheckVar1)
    w = Label(top, text="       OR      ")
    w.pack()
    cc2 = Checkbutton(top, text = "Load Ram Image", variable = CheckVar2)
    cc1.pack()
    cc2.pack()
    def quits():
        jok=open("checkme.txt","w")
        v1=
    Button(top, text="Click me to record changes.", command=quits).pack()
    top.mainloop()
    """
    ###################
    root = Tk()
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'selected_dlllist.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'selected_handles.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'pslistinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'pstreeinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'psxviewinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'psscan_dot.dot')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'serviceinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'malfindinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'mftparserinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'networkinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'privsinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'driverscaninf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'filescaninf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'modscaninf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'modules.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'ssdtinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'symlinkscaninf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'unloadedmodulesinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'alldlllistinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'allhandlesinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'allcallbacksinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'alltimersinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'malfinddiff.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'modulesinf.txt')
    except:
        pass
    try:
        os.remove(os.getcwd()+os.sep+'Database'+os.sep+'Analyzed_RAM_artifacts'+os.sep+'ssdtdiff.txt')
    except:
        pass
    
    root.iconbitmap(default='favicon.ico')
    root.geometry("700x800+10+10")
    #root.configure(background='black')
    #root.update()
    #root["bg"]="black"
    app = Example(root)
    #root.configure(background='black')
    """
    im = Image.open('favicon.ico')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Tkinter.Label(root,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    """
    root.mainloop()  

