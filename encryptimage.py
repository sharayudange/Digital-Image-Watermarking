from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image,ImageTk

def submit1():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image",
                                     filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png")))
    nimg = fln.split(".")[0]+"_encrypted.png"
    img = Image.open(fln)
    img.thumbnail((140, 240))
    img = ImageTk.PhotoImage(img)
    lbl.config(image=img)
    lbl.image = img
    ipath = fln
    dtext = data.get()
    import main
    a = main.ImageSteg()
    try:
        a.encrypt_text_in_image(ipath, dtext)
        message.set("New image has been created with data encrypted in it")
        img = Image.open(nimg)
        img.thumbnail((140, 240))
        img = ImageTk.PhotoImage(img)
        lbl1.config(image=img)
        lbl1.image = img
    except:
        message.set("Unable to find image on given path!! please try again !!")


screen = Tk()
screen.title("Encrypt Image")
screen.geometry("900x900")
message = StringVar()
img_path=StringVar()
data = StringVar()
Label(screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()


Label(screen, text="Data to be encrypted * ").place(x=20,y=80)
Entry(screen, textvariable=data,show="*").place(x=180,y=82)
Label(screen, text="",textvariable=message).place(x=95,y=100)
Button(screen, text="Encrypt", width=10, height=1, bg="orange",command=submit1).place(x=105,y=130)

lbl = tk.Label(screen)
lbl.place(x=550,y=10,anchor='w')
lbl.pack()
Label(text="original image",bg="blue",fg="white")
Label(text="").place()

lbl1 = tk.Label(screen)
lbl1.place(x=550,y=120,anchor='w')
lbl1.pack()

screen.mainloop()