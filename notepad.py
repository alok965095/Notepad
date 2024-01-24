from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root=Tk()
root.title("Untitled -Notepad")
root.geometry("544x600")
# Adding command
def new_file():
    global file
    root.title("Notepad")
    file = None
    text_area.delete(1.0,END)
def open_file():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file  = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0,END)
        f = open(file,"r")
        text_area.insert(1.0,f.read())
        f.close()


def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(text_area.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
def qui():
    root.destroy()

def cut():
    text_area.event_generate(("<<Cut>>"))
def copy():
    text_area.event_generate(("<<Copy>>"))
def paste():
    text_area.event_generate(("<<Paste>>"))
def about():
    messagebox.showinfo("Notepad","Notepad created by Alok")
def light():
    text_area.config(background="white",foreground="black")
    
def dark():
    text_area.config(background="black",foreground="white")
    root.config(bg = "black")
 
# text area
text_area = Text(root,font="verdana 12 ")
text_area.pack(expand=True,fill=BOTH)
file = None
# Adding scrollbar
scroll = Scrollbar(text_area)
scroll.pack(side = RIGHT,fill=Y)
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)
# menu bar 
menu_bar = Menu(root)
file_bar = Menu(menu_bar,tearoff=0)
file_bar.add_command(label="New",command=new_file)
file_bar.add_command(label="Open",command=open_file)
file_bar.add_command(label="Save",command=save_file)
file_bar.add_separator()
file_bar.add_command(label="Exit",command=qui)
menu_bar.add_cascade(label="File",menu = file_bar)

edit_bar = Menu(menu_bar,tearoff=0)
edit_bar.add_command(label="Cut",command=cut)
edit_bar.add_command(label="Copy",command=copy)
edit_bar.add_command(label="Paste",command=paste)
menu_bar.add_cascade(label="Edit",menu = edit_bar)

the_bar = Menu(menu_bar,tearoff=0)
the_bar.add_command(label="Light",command=light)
the_bar.add_command(label="Dark",command=dark)
menu_bar.add_cascade(label="Theme",menu = the_bar)

help_bar = Menu(menu_bar,tearoff=0)
help_bar.add_command(label="about",command=about)
menu_bar.add_cascade(label="Help",menu = help_bar)

root.config(menu=menu_bar)
root.mainloop()