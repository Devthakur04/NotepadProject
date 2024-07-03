from tkinter import *
from tkinter.messagebox import showinfo
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename

def new():
    global file
    root.title("Untitled-Notepad")
    file=None
    textarea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
def exitfile():
    root.destroy()
def cut():
    textarea.event_generate(("<>"))
def copy():
    textarea.event_generate(('<>'))
def paste():
    textarea.event_generate(("<>"))
def helpfile():
    showinfo('Notepad','Notepad by DS')

if __name__=="__main__":
    root=Tk()
    root.title("Untitled-Notepad")
    root.geometry("744x888")
    

    textarea=Text(root,font='lucida 13')
    file=None
    textarea.pack(expand=True,fill=BOTH)

    

    Menubar=Menu(root)
    Filemenu=Menu(Menubar,tearoff=0)
    Filemenu.add_command(label='New',command=new)
    Filemenu.add_command(label='open',command=openfile)
    Filemenu.add_command(label='save',command=save)
    Filemenu.add_separator()
    Filemenu.add_command(label='exit',command=exitfile)
    Menubar.add_cascade(label='file',menu=Filemenu)

    Editmenu=Menu(root)
    Editmenu=Menu(Menubar,tearoff=0)
    Editmenu.add_command(label='cut',command=cut)
    Editmenu.add_command(label='copy',command=copy)
    Editmenu.add_command(label='paste',command=paste)
    Menubar.add_cascade(label='Edit',menu=Editmenu)

    Helpmenu=Menu(root)
    Helpmenu=Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label='help',command=helpfile)
    Menubar.add_cascade(label='help',menu=Helpmenu)

    root.config(menu=Menubar)

    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)



    root.mainloop()
