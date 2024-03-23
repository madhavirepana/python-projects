from PyPDF2 import*
from tkinter import*
from tkinter.filedialog import*
from tkinter import messagebox
import os.path as pd
import tkinter as tk
from tkinter import filedialog
fd=""
    
filterex=(
        ('PDF File','*.pdf'),
        ('Doc Files','*.docx')
    )
                
def split_file():
    global fd
    if fd.endswith(".pdf"):
        pages=tb3.get().split("-")
        startIndex=int(pages[0])
        endIndex=int(pages[-1])    
        with open(fd,'rb')as fp:
            rd=PdfReader(fp)
            wd=PdfWriter()
            for i in range(startIndex-1,endIndex):
                cpage=rd.pages[i]
                wd.add_page(cpage)
            with open("result.pdf","wb") as nf:
                wd.write(nf)
        if pd.exists("result.pdf"):
            messagebox.showinfo('split pdf',"PDF split has been done successfully.\n")
            
    elif fd.endswith(".docx"):
        try:
            with open(input_file, 'rb') as f:
                content = f.read()
                total_size = len(content)
                part_size = total_size // num_parts

                for i in range(num_parts):
                    start = i * part_size
                    end = (i + 1) * part_size if i < num_parts - 1 else total_size

                    output_file = f"{pd.splitext(input_file)[0]}_part{i + 1}.txt"
                    with open(output_file, 'wb') as part_file:
                        part_file.write(content[start:end])

                print(f"File split into {num_parts} parts successfully.")
        except Exception as e:
            print(f"Error splitting file: {str(e)}")
        input_file = label2.get()
        num_parts = int(label2.get())

        if pd.isfile(input_file) and num_parts > 0:
            split_file(input_file, num_parts)
        else:
            print("Invalid input. Please provide a valid file and a positive number of parts.")
            
def clear_file():
            tb1.delete(0,END)
            tb2.delete(0,END)
            tb3.delete(0,END)
        
r=Tk()
r.title('Split PDF using Tkinter Python')
r.geometry('810x520')
r.resizable(False,False)

label1=Label(r,text="Split file",fg='blue',font="Helvetica 24 bold")
label1.grid(row=0,column=1)

label2=Label(r,text="Select PDF file: ")
label2.grid(row=1,column=0)

tb1=Entry(r,width=90)
tb1.grid(row=1,column=1,ipadx=5,ipady=5)

def show_file():
    global fd
    fd= filedialog.askopenfilename(filetypes=[("Text Files", ".pdf"), ("All Files", ".docx")])
    if fd.endswith(".pdf"):
        tb1.delete(0,END)
        tb1.insert(0,fd)
        with open(fd,"rb") as file:
            pr=PdfReader(file)
            totalpages=len(pr.pages)
            tb2.insert(0,totalpages)
            
    elif fd.endswith(".docx"):
        
        label2.delete(0,tk.END)
        label2.insert(0, fd)

b1=Button(r,text="Browse PDF",bg="red",fg="white",command=show_file,width=13)
b1.grid(row=1,column=2,ipadx=5,ipady=5)

label3=Label(r,text="total pages: ")
label3.grid(row=2,column=0)

tb2=Entry(r,width=90)
tb2.grid(row=2,column=1,ipadx=5,ipady=5)

label4=Label(r,text="select pages from: ")
label4.grid(row=5,column=0,ipady=10)

tb3=Entry(r,width=90)
tb3.grid(row=5,column=1,ipadx=5,ipady=5)

b2=Button(r,text="split pdf",bg="green",fg="white",width=15,command=split_file)
b2.grid(row=7,column=1,ipadx=5,ipady=5,pady=5)

ct=Button(r,text="Clear",bg="gray",fg="white",width=15,command=clear_file())
ct.grid(row=9,column=1,ipadx=5,ipady=5,pady=5)

r.mainloop()         
