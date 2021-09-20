from tkinter import *
from tkinter import messagebox, filedialog
import os
import shutil

root = Tk()
root.title("FileExplorer")
root.iconbitmap('Favicon.ico')
root.geometry("600x600")
root.config(background="Lime")

def Open():
    file = filedialog.askopenfilename()
    if file:
        os.startfile(file)

def Delete():
    file = filedialog.askopenfilename()
    if file:
        os.remove(file)
        messagebox.showinfo("Delete", file+" Deleted Successfully")

def Rename():
    global fileName, path, frame
    file = filedialog.askopenfilename()
    if file:
        path = os.path.abspath(file)
        frame = Frame(root,padx=40,pady=40)
        frame.place(x=80,y=450)
        fileName = Entry(frame,width=50)
        fileName.grid(row=1,column=0)
        fileName.insert(0,"Enter the new name")
        Button(frame,text="Rename",width=10,command=change).place(x=1,y=30)
        Button(frame, text="Cancel", width=10,command=frame.destroy).place(x=220,y=30)
        frame.mainloop()

def change():
    newName = fileName.get()
    Dir = os.path.dirname(path)
    changeName = os.path.join(Dir, newName)
    os.rename(path, changeName)
    frame.destroy()
    messagebox.showinfo("Rename", "The file is renamed successfully")

def Copy():
    global source, destination, frame2
    frame2 = Frame(root, padx=35, pady=40)
    frame2.place(x=10, y=435)
    Label(frame2, text="Source",font=("Georgia",12)).grid(row=1,column=0, pady=(0,10))
    Label(frame2, text="Destination", font=("Georgia", 12) ).grid(row=2, column=0, pady=(0,10))
    source = Entry(frame2, width=50)
    source.grid(row=1, column=1, pady=(0,10), padx=(0,10))
    destination = Entry(frame2, width=50)
    destination.grid(row=2, column=1, pady=(0,10), padx=(0,10))
    sourceBtn = Button(frame2, text="Browse", width=10, font=("Georgia",12), command=sourceBrowse)
    sourceBtn.grid(row=1,column=2, pady=(0,10))
    destinationBtn = Button(frame2, text="Browse", width=10, font=("Georgia", 12), command=destinationBrowse)
    destinationBtn.grid(row=2, column=2, pady=(0,10))
    Button(frame2, text="Copy", width=10, command=copyFile).place(x=1, y=80)
    Button(frame2, text="Cancel", width=10, command=frame2.destroy).place(x=220, y=80)
    frame2.mainloop()

def Move():
    global source, destination, frame2
    frame2 = Frame(root, padx=35, pady=40)
    frame2.place(x=10, y=435)
    Label(frame2, text="Source",font=("Georgia",12)).grid(row=1,column=0, pady=(0,10))
    Label(frame2, text="Destination", font=("Georgia", 12) ).grid(row=2, column=0, pady=(0,10))
    source = Entry(frame2, width=50)
    source.grid(row=1, column=1, pady=(0,10), padx=(0,10))
    destination = Entry(frame2, width=50)
    destination.grid(row=2, column=1, pady=(0,10), padx=(0,10))
    sourceBtn = Button(frame2, text="Browse", width=10, font=("Georgia",12), command=sourceBrowse)
    sourceBtn.grid(row=1,column=2, pady=(0,10))
    destinationBtn = Button(frame2, text="Browse", width=10, font=("Georgia", 12), command=destinationBrowse)
    destinationBtn.grid(row=2, column=2, pady=(0,10))
    Button(frame2, text="Move", width=10, command=moveFile).place(x=1, y=80)
    Button(frame2, text="Cancel", width=10, command=frame2.destroy).place(x=220, y=80)
    frame2.mainloop()

def sourceBrowse():
    file = filedialog.askopenfilename()
    source.insert(0, file)

def destinationBrowse():
    folder = filedialog.askdirectory()
    destination.insert(0, folder)

def copyFile():
    src = source.get()
    des = destination.get()
    shutil.copy(src,des)
    messagebox.showinfo("Copy File", "File copied successfully")
    frame2.destroy()

def moveFile():
    src = source.get()
    des = destination.get()
    shutil.move(src,des)
    messagebox.showinfo("Copy File", "File moved successfully")
    frame2.destroy()

def Create():
    global Dir1, folderName, frame3
    Dir1 = filedialog.askdirectory()
    if Dir1:
        frame3 = Frame(root, padx=35, pady=40)
        frame3.place(x=10, y=435)
        Label(frame3, text="Name", font=("Georgia", 12)).grid(row=1, column=0, pady=(0, 10))
        folderName = Entry(frame3, width=50)
        folderName.grid(row=1, column=1, pady=(0, 10), padx=(0, 10))
        Button(frame3, text="Create", width=10, command=createfolder).grid(row=1, column=2, pady=(0, 10))
        Button(frame3, text="Cancel", width=10, command=frame3.destroy).place(x=220, y=40)
        frame3.mainloop()

def createfolder():
    name = folderName.get()
    os.chdir(Dir1)
    os.makedirs(name)
    frame3.destroy()
    messagebox.showinfo("Create Folder", name+" folder is created")

def DeleteFolder():
    Dir = filedialog.askdirectory()
    if Dir:
        os.rmdir(Dir)
        messagebox.showinfo("Delete Folder", "The Folder is Deleted!")

def RenameFolder():
    global  frame4, path1, folderName1
    folder = filedialog.askdirectory()
    if folder:
        path1 = os.path.abspath(folder)
        frame4 = Frame(root, padx=35, pady=40)
        frame4.place(x=10, y=435)
        Label(frame4, text="Name", font=("Georgia", 12)).grid(row=1, column=0, pady=(0, 10))
        folderName1 = Entry(frame4, width=50)
        folderName1.grid(row=1, column=1, pady=(0, 10), padx=(0, 10))
        Button(frame4, text="Create", width=10, command=Folder_Name).grid(row=1, column=2, pady=(0, 10))
        Button(frame4, text="Cancel", width=10, command=frame4.destroy).place(x=220, y=40)
        frame4.mainloop()

def Folder_Name():
    newFolder = folderName1.get()
    Dir2 = os.path.dirname(path1)
    Rename_fol = os.path.join(Dir2, newFolder)
    os.rename(path1, Rename_fol)
    frame4.destroy()
    messagebox.showinfo("Rename Folder", "The Folder is renamed successfully")


title = Label(root, text="Welcome to FileExplorer",font=("Georgia",16),bg="Lime")
title.place(x=170,y=50)

open = Button(root,text="Open File",width=15,font=("Georgia",14),command=Open)
open.grid(row=1,column=1,padx=50,pady=(150,20))

delete = Button(root,text="Delete a File",width=15,font=("Georgia",14),command=Delete)
delete.grid(row=1,column=2,padx=60,pady=(150,20))

rename = Button(root,text="Rename File",width=15,font=("Georgia",14),command=Rename)
rename.grid(row=2,column=1,padx=50,pady=20)

copy = Button(root,text="Copy a File",width=15,font=("Georgia",14), command=Copy)
copy.grid(row=2,column=2,padx=60,pady=20)

move = Button(root,text="Move a File",width=15,font=("Georgia",14), command=Move)
move.grid(row=3,column=1,padx=50,pady=20)

createFolder = Button(root,text="Create a Folder",width=15,font=("Georgia",14), command=Create)
createFolder.grid(row=3,column=2,padx=60,pady=20)

deleteFolder = Button(root,text="Delete a Folder",width=15,font=("Georgia",14), command=DeleteFolder)
deleteFolder.grid(row=4,column=1,padx=50,pady=20)

renameFolder = Button(root,text="Rename Folder",width=15,font=("Georgia",14), command=RenameFolder)
renameFolder.grid(row=4,column=2,padx=60,pady=20)


root.mainloop()