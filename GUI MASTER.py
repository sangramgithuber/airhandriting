

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

image2=Image.open("AirWriting-WHITELC.jpg")
image2=image2.resize((1600,800),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

frame=Frame(root,bg="white")
frame.place(x=0,y=0,height=30,width=1700)

label =Label(root, text="AIR WRITING USING EFFECTIVE MACHINE LEARNING TECHNIQUE", font=("times new roman", 31), bg="gray80",fg="black")
label.place(x=0, y=0,width=1590)

def reg():
    from subprocess import call
    call(["python","home.py"])
    
    
def log1():
        from subprocess import call
        call(["python","features.py"])
        
def log2():
    from subprocess import call
    call(["python","finger.py"]) 
    
def log3():
    from subprocess import call
    call(["python","draw.py"]) 
    
# def log4():
#     from subprocess import call
#     call(["python","HandTrackingModule.py"]) 
    
def log5():
    from subprocess import call
    call(["python","virtual_shape.py"]) 
########################################## ADD BUTTON ###############################################################
registration_button = tk.Button(root, text="HOME PAGE",command=reg,font=("Helvetica", 18, "bold"), bg="gray90", fg="green",bd=4)
registration_button.place(x=150, y=300, height=40, width=200)


login_button = tk.Button(root, text="Features",command=log1,font=("Helvetica", 18, "bold"), bg="gray90", fg="green",bd=4)
login_button.place(x=400, y=300, height=40, width=300)

# login_button = tk.Button(root, text="Air handwriting Page",command=log2,font=("Helvetica", 18, "bold"), bg="gray90", fg="green",bd=4)
# login_button.place(x=750, y=400, height=40, width=400)

login_button = tk.Button(root, text="Air handwriting Draw",command=log2,font=("Helvetica", 18, "bold"), bg="gray90", fg="green",bd=4)
login_button.place(x=200, y=400, height=40, width=400)

login_button = tk.Button(root, text="Air handwriting Virtual Shapes",command=log5,font=("Helvetica", 18, "bold"), bg="gray90", fg="green",bd=4)
login_button.place(x=700, y=400, height=40, width=500)

login_button = tk.Button(root, text="Air handwriting HandTracking Module",command=log3,font=("Helvetica", 18, "bold"), bg="gray90", fg="green",bd=4)
login_button.place(x=750, y=300, height=40, width=700)



exit_button = tk.Button(root, text="Exit", font=("Helvetica", 18, "bold"), bg="gray90", fg="red",command=root.quit)
exit_button.place(x=580, y=530, height=35, width=142)

root.mainloop()