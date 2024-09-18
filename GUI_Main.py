from tkinter import *
import tkinter
import tkinter as tk

from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk,Image
import re

root=tk.Tk()

root.configure(background="white")

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

root.title("Home page")

image2=Image.open("A3.webp")
image2=image2.resize((1600,800),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

frame=Frame(root,bg="white")
frame.place(x=0,y=0,height=30,width=1700)

label =Label(root, text="AIR WRITING USING EFFECTIVE MACHINE LEARNING TECHNIQUE", font=("times new roman", 31), bg="gray80",fg="black")
label.place(x=0, y=0,width=1530)

def reg():
    from subprocess import call
    call(["python","registration.py"])
    
def log():
    from subprocess import call
    call(["python","Air_login.py"]) 
########################################## ADD BUTTON ###############################################################
registration_button = tk.Button(root, text="Registration",command=reg,font=("Helvetica", 18, "bold"), bg="gray90", fg="green")
registration_button.place(x=400, y=670, height=35, width=142)

login_button = tk.Button(root, text="Login",command=log,font=("Helvetica", 18, "bold"), bg="gray90", fg="green")
login_button.place(x=700, y=670, height=35, width=142)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 18, "bold"), bg="gray90", fg="red",command=root.quit)
exit_button.place(x=1000, y=670, height=35, width=142)

root.mainloop()