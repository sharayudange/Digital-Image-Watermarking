from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image,ImageTk

def submit1():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image",
                                     filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png")))
    ipath = fln
    dtext = data.get()
    import main
    a = main.ImageSteg()
    try:
        b=a.decrypt_text_in_image(ipath)
        if b==dtext:
            message.set("Data Matched on the image")
        else:
            message.set("Data didn't matched on the image")
    except:
        message.set("Unable to find image on given path!! please try again !!")

from tkinter import *
screen = Tk()
screen.title("Match Data")
screen.geometry("500x300")
message = StringVar()
img_path=StringVar()
data = StringVar()
Label(screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()

Label(screen, text="Expected data to be found * ").place(x=20,y=80)
Entry(screen, textvariable=data,show="*").place(x=180,y=82)
Label(screen, text="",textvariable=message).place(x=95,y=100)
Button(screen, text="Decrypt", width=10, height=1, bg="orange",command=submit1).place(x=105,y=130)
screen.mainloop()