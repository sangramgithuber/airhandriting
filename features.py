

import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()



#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))






Height = tk.IntVar()
Weight = tk.IntVar()

def main():
    h = Height.get()
    w = Weight.get()
    

image2 = Image.open('home.jpg')
image2 = image2.resize((1500, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



lbl = tk.Label(root, text="Features of Air handwriting", font=('Lucida Sans Unicode', 40,' bold ',), height=1, width=50,bg="black",fg="white")
lbl.place(x=0, y=3)





        
Login_frame=tk.Frame(root)
Login_frame.place(x=190,y=120)     
lbluser=tk.Label(Login_frame,text="  Air Writing Recognition: \n Recognize and interpret gestures made in the air to convert them into written text.",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
#++++++++++++++++++++++++++++++++++++++++++++++++



Login_frame=tk.Frame(root)
Login_frame.place(x=350,y=250)   
lbluser=tk.Label(Login_frame,text="Real-Time Feedback: \n Offer real-time feedback as users write in the air, \n helping them adjust their gestures for optimal recognition. ",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
#++++++++++++++++++++++++++++++++++++++++++++




Login_frame=tk.Frame(root)
Login_frame.place(x=200,y=400)      
lbluser=tk.Label(Login_frame,text="Educational Mode: \n Provide an educational mode to help users learn and improve their air handwriting skills,\n offering guidance and tips.",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
#++++++++++++++++++++++++++++++++++++++++++++


Login_frame=tk.Frame(root)
Login_frame.place(x=100,y=550)
lbluser=tk.Label(Login_frame,text="Security Measures: \n Implement security measures to protect user data and ensure that air handwriting interactions are secure. ",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)



         


root.mainloop()