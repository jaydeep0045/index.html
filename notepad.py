from tkinter import *

def myFunc():
    pass

def newWindow():
    open("notepad.py")
    # print("new window")

root = Tk()
root.title("Untitled - Notepad")
root.geometry("1000x475")

# for notepad icon
root.wm_iconbitmap("notepad1.jpg")
root.config()

# for a notepad logo
mainMenu = Menu(root)
m1 = Menu(mainMenu,tearoff=0)
m1.add_command(label="New",command=myFunc)
m1.add_command(label="New Window",command=newWindow)
m1.add_command(label="Open..",command=myFunc)
m1.add_command(label="Save",command=myFunc)
m1.add_command(label="Save As",command=myFunc)
m1.add_separator()
m1.add_command(label="Page Setup...",command=myFunc)
m1.add_command(label="Print...",command=myFunc)
m1.add_separator()
m1.add_command(label="Exit",command=exit)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="File",menu=m1)


m2 = Menu(mainMenu,tearoff=0)
m2.add_command(label="Undo",command=myFunc)
m2.add_separator()
m2.add_command(label="Cut",command=myFunc)
m2.add_command(label="Copy",command=myFunc)
m2.add_command(label="Paste",command=myFunc)
m2.add_command(label="Delete",command=myFunc)
m2.add_separator()
m2.add_command(label="Search with Bing",command=myFunc)
m2.add_command(label="Find",command=myFunc)
m2.add_command(label="Find Next",command=myFunc)
m2.add_command(label="Find Previous",command=myFunc)
m2.add_command(label="Replace...",command=myFunc)
m2.add_command(label="Go To...",command=myFunc)
m2.add_separator()
m2.add_command(label="Select All",command=myFunc)
m2.add_command(label="Time/Date...",command=myFunc)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainMenu,tearoff=0)
m3.add_checkbutton(label="Word Wrap")
m3.add_command(label="Font...",command=myFunc)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Format",menu=m3)

m4 = Menu(mainMenu,tearoff=0)
m4.add_command(label="Zoom",command=myFunc)
m4.add_checkbutton(label="Status Bar")
root.config(menu=mainMenu)
mainMenu.add_cascade(label="View",menu=m4)

m5 = Menu(mainMenu,tearoff=0)
m5.add_command(label="View Help",command=myFunc)
m5.add_command(label="Send Feedback",command=myFunc)
m5.add_separator()
m5.add_command(label="About Notepad",command=myFunc)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Help",menu=m5)

# for a scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=BOTH)

text = Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

StatusVar = StringVar()
StatusVar.set("Ln 1, Col 1\t100%\tWindows(CRLF)\tUTF-8")
Status_Bar = Label(root,textvariable=StatusVar,relief=SUNKEN,anchor="e",padx=20)
Status_Bar.pack(fill=X,side=BOTTOM)

root.mainloop()