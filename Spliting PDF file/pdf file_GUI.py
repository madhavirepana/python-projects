#with GUI applications
#----------------------

from PyPDF2 import*
from tkinter import*
from tkinter.filedialog import*
from tkinter import messagebox
import os.path as pd

#create a tkinter root window using Tk() method
r=Tk()
r.title('Split PDF using Tkinter Python')
r.geometry('810x320')
#Disable the maximize window
r.resizable(False,False)
#now add widgets Label,Buttons,Text box one by one
label1=Label(r,text="Split PDF file",fg='blue',font="Helvetica 24 bold")
#add label to window using grid manager
label1.grid(row=0,column=1)
label2=Label(r,text="Select PDF file: ")
label2.grid(row=1,column=0)
#add first text box
tb1=Entry(r,width=90)
#add first text box to root window using grid() manager
tb1.grid(row=1,column=1,ipadx=5,ipady=5)
#declare variable in global scope
fd=""
#code for browse button
def showPDF():
    global fd
#start the open dialog
    fd=askopenfilename(title="open PDF file")
#display the selected pdf file in first text box named tb1 using insert(index,text)
    tb1.insert(0,fd)
#also display the total no of pages
#use python file concept to open file
#fd contains the path of selected pdf file,so just give it as a first arguement in the open function
    with open(fd,"rb") as file:
        pr=PdfReader(file)
# now we use built in function property
        totalpages=len(pr.pages)
#display the total pages in second text box named tb2 using same instance method insert(index.text)
        tb2.insert(0,totalpages)

b1=Button(r,text="Browse PDF",bg="red",fg="white",command=showPDF,width=13)
b1.grid(row=1,column=2,ipadx=5,ipady=5)
label3=Label(r,text="total pages: ")
label3.grid(row=2,column=0)
tb2=Entry(r,width=90)
#ipadx,ipady are paddings  which are optional
tb2.grid(row=2,column=1,ipadx=5,ipady=5)
label4=Label(r,text="select pages from: ")
label4.grid(row=3,column=0)
tb3=Entry(r,width=90)
tb3.grid(row=3,column=1,ipadx=5,ipady=5)
#grid provides row and column properties to arrange widgets
#code for split
def splitTask():
    global fd
#split function returns list objects
    pages=tb3.get().split("-")
    startIndex=int(pages[0])
    endIndex=int(pages[-1])
    
#now read the selected pdf file here in read mode which is refered by fd object    
    with open(fd,'rb')as fp:
#also open reader and writer pdf classes
        rd=PdfReader(fp)
        wd=PdfWriter()
#now use for loop to get pages one by one
        for i in range(startIndex-1,endIndex):
#get the selected pdf content using reader pdf class
            cpage=rd.pages[i]
#add this pdf content to pdf writer class object using its instance method add_page(any)
#this process continue till end of the page number
            wd.add_page(cpage)
#now write entire pdf collection to new pdf file in current directory
#use write() method to write contents of pdf writer class to python file object nf
        with open("result.pdf","wb") as nf:
            wd.write(nf)
#now check whether new splitted pdf  is creator or not using exists() method path module
    if pd.exists("result.pdf"):
        messagebox.showinfo('split pdf',"PDF split has been done successfully.\n")
b2=Button(r,text="split pdf",bg="green",fg="white",width=15,command=splitTask)
b2.grid(row=4,column=1,ipadx=5,ipady=5,pady=5)

def clearUI():
    tb1.delete(0,END)
    tb2.delete(0,END)
    tb3.delete(0,END)
    
ct=Button(r,text="Clear",bg="gray",fg="white",width=15,command=clearUI)
ct.grid(row=5,column=1,ipadx=5,ipady=5,pady=5)

#add this button to root window next to split button

r.mainloop()         


