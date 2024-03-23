from PyPDF2 import*
from tkinter import*
from tkinter.filedialog import*
from tkinter import messagebox
import os.path as pd
import os.path


filterex=(
        ('PDF File','*.pdf'),
        ('Doc Files','*.docx')
    )

    
def show_file():
    global fd
    if fd.endswith(".pdf"):
        tb1.delete(0,END)
        tb1.insert(0,fd)
        with open(fd,"rb") as file:
            pr=PdfReader(file)
            totalpages=len(pr.pages)
            tb2.insert(0,totalpages)
    elif fd.endswith(".docx"):
        tb1.delete(0,END)
        tb2.insert(0,fd)
                
def split_file():
    # global fd
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
            def clear_file():
                tb1.delete(0,END)
                tb2.delete(0,END)
                tb3.delete(0,END)
    elif fd.endswith(".docx"):
        with open(fd, 'rb') as f:
            fd = f.read()
            total_size = len(pages)
            part_size = total_size //split_file

        for i in range(startIndex-1,endIndex):
            start = i * part_size
            end = (i + 1) * part_size if i <  - 1 else total_size

            output_file = f"{pd.splitext(fd)[0]}_page{i + 1}.txt"
            with open(output_file, 'wb') as part_file:
                part_file.write(pages[start:end])

        print(f"File split into {split_file} parts successfully.")
def clear_file():
    if pd.exists("result.pdf"):
        tb1.delete(0,END)
        tb2.delete(0,END)
        tb3.delete(0,END)
    elif pd.endswith(".docx"):
        input_file = tb1.get()
        num_parts = int(tb2.get())

        if pd.isfile(input_file) and num_parts > 0:
            split_file(input_file, num_parts)
        else:
            print("Invalid input. Please provide a valid file and a positive number of parts.") 

r=Tk()
r.title('Split PDF using Tkinter Python')
r.geometry('810x520')
r.resizable(False,False)

label1=Label(r,text="Split PDF file",fg='blue',font="Helvetica 24 bold")
label1.grid(row=0,column=1)

label2=Label(r,text="Select PDF file: ")
label2.grid(row=1,column=0)

tb1=Entry(r,width=90)
tb1.grid(row=1,column=1,ipadx=5,ipady=5)

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


ct=Button(r,text="Clear",bg="gray",fg="white",width=15,command=clear_file)
ct.grid(row=9,column=1,ipadx=5,ipady=5,pady=5)
fd=askopenfilename(title="open PDF file", filetype=filterex)

r.mainloop()         
