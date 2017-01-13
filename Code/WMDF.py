import sys
from Tkinter import *

import ramimage
import compareartifacts


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

    def initUI(self):
      
        self.parent.title("Windows MemDiff Forensics Tool")

    

def mainc():
    fl=open('choice.txt','w')
    fl.close()
    
    root = Tk()
    root.iconbitmap(default='favicon.ico')
    root.geometry("350x100+10+10")
    
    
    
     

    app = Example(root)

    v = IntVar()

    Radiobutton(root, text="Analyze Ram Image", variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text="Compare Memory artifacts", variable=v, value=2).pack(anchor=W)
    def record():
        fl=open('choice.txt','w')
        fl.write(str(v.get()))
        fl.close()
        root.destroy()
    record=Button(root, text="OK",command=record)
    record.place(x=200, y=10)
    #root.after(7500, lambda: root.destroy())
    root.mainloop() 
    """
    print
    print
    print
    global aaa
    aaa=raw_input("Press 1 to Analyze Ram Image...\nPress 2 to Compare artifacts...\nPress any other button to exit.. ")
    
    try:
        aaa=int(aaa)
    except:
        sys.exit(0)
    if aaa!=1 and aaa!=2:
        print 'Thanks..'
        sys.exit(0)
    if aaa==1:
        ramimage.mainc()
    if aaa==2:
        compareartifacts.mainc()
    """
mainc()

fl=open('choice.txt','r')
textt=fl.read().strip()
fl.close()
if textt=='1':
    ramimage.mainc()
elif textt=='2':
    compareartifacts.mainc()
else:
    pass
