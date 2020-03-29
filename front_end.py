from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from controller import trigger


# creates welcome window
welcome = Tk()


# add widgets here


# creates choose file button and defines the openFile command
def openFile():
    selectedfile = filedialog.askopenfilename(initialdir="./", title="Select A File", filetypes=(("CSV files", "*.csv"),("all files", "*.*")))
    fname.delete(0, END)
    fname.insert(0, selectedfile)

def printtester():
    print(fname.get())

def submitaction():
    if (not fname.get()[-4:] == ".csv"):
        messagebox.showinfo("Error!", "Selected file is not a CSV")
    else:
        trigger(fname.get())



select_file_btn = Button(welcome, text="Select a File", fg='white', bg='gray', command=openFile)
select_file_btn.place(relx=0.8, rely=0.77, anchor=W)

# creates submit button - currently only closes the window, needs to be updated to actually run the data manipulation function
submit = Button(welcome, text="Submit", fg='white', bg='gray', width=10, command=submitaction)
submit.place(relx=0.4, rely=0.9, anchor=CENTER)

# creates cancel button
cancel_btn = Button(welcome, text='Cancel', fg='white', bg='gray', width=10, command=welcome.destroy)
cancel_btn.place(relx=0.6, rely=0.9, anchor=CENTER)

# creates tool label - ISM CSV Grapher Tool
tool_lbl = Label(welcome, text="USACE Invasive Species Management CSV Grapher Tool", fg='black', font=("Times New Roman", 16))
tool_lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

# creates description of tool that is split into three labels because i cant figure out text wrapping
description_lbl1 = Label(welcome, text="The purpose of this tool is to effectively read and graph various CSV files.")
description_lbl1.place(relx=0.5, rely=0.2, anchor=CENTER)
description_lbl2 = Label(welcome, text="This application will hopefully save you time in the long run.")
description_lbl2.place(relx=0.5, rely=0.25, anchor=CENTER)
description_lbl3 = Label(welcome, text="Please enter your filepath in the entry box below or click Select a File.")
description_lbl3.place(relx=0.5, rely=0.3, anchor=CENTER)

# creates entry instruction label
instr = Label(welcome, text="Enter file path: ")
instr.place(relx=0.1, rely=0.7)

# creates entry widget
fname = Entry(welcome, width=80)
fname.place(relx=0.1, rely=0.75)

welcome.title('USACE CSV Grapher Tool')
welcome.geometry("700x500+10+20")
welcome.mainloop()
