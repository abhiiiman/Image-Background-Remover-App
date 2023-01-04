# importing the required modules here.
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os, sys
from rembg import remove

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# creating the button functions here.
def upload_image():
    global filename

    try:
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
        title="Select Image File", filetype = (("PNG file", "*.png"),
                                                ("JPG file", "*.jpg"),
                                                ("ALL file", "*.txt")))
        img = Image.open(filename)
        img = img.resize((240, 230))
        img = ImageTk.PhotoImage(img)

        lbl1.configure(image = img, width = 240, height = 230)
        lbl1.image = img
    
    except:
        messagebox.showerror("Error", "There was a problem Loading your File, Try Again 😥")

def remove_bg():
    global output

    try:
        input_path = filename
        input = Image.open(input_path)
        messagebox.showinfo("Task In Progress...", "Removing The Background, Please Wait 😎")
        output = remove(input)
        output.save("temp.png")

        img = Image.open("temp.png")
        img = img.resize((240, 230))
        img = ImageTk.PhotoImage(img)

        lbl2.configure(image = img, width = 240, height = 230)
        lbl2.image = img
    
    except:
        messagebox.showwarning("File Not Found for Operation", "Please Select An Image With Human Face First 😕")


def download_image():
    try:
        file = filedialog.asksaveasfilename(initialdir=os.getcwd(), filetypes=[("PNG file", "*.png"), ("JPG file", "*.jpg")], defaultextension='.png')
        output_path = f"{file}"
        output.save(output_path)
        messagebox.showinfo("File Saved", "Image Saved Successfully 😊")
    except:
        messagebox.showwarning("File Not Found to Download", "Please Select An Image With Human Face First 😕")

window = Tk()
window.title("Background Remover")
width = 800
height = 520
window.geometry(f"{width}x{height}")
window.configure(bg = "#fedf86")
window.iconbitmap(resource_path("logo.ico"))
window.resizable(False, False)

canvas = Canvas(window,bg = "#fedf86",height = 982,width = 1512,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

# placing the window at the center of the screen here.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width / 2)
y_coordinate = (screen_height / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

background_img = PhotoImage(file = resource_path("background.png"))
background = canvas.create_image(400, 260,image=background_img)

img0 = PhotoImage(file = resource_path("img0.png"))
b0 = Button(image = img0,borderwidth = 0,command = upload_image, bg = "#E573E1", activebackground ="#E573E1")
b0.place(x = 268, y = 440,width = 25,height = 25)

img1 = PhotoImage(file = resource_path("img1.png"))
b1 = Button(image = img1,borderwidth = 0,command = download_image, bg = "#CEFB02", activebackground = '#CEFB02')
b1.place(x = 652, y = 440,width = 25,height = 25)

img2 = PhotoImage(file = resource_path("img2.png"))
b2 = Button(image = img2,borderwidth = 0,command = remove_bg,bg = '#F99597', activebackground = '#F99597')
b2.place(x = 375, y = 260,width = 50,height = 50)

# creating the select image frame here.
selectimage = Frame(canvas, width = 240, height = 230, bg = "black", relief = GROOVE, border=10)
selectimage.place(x = 83, y = 165)
# creating the label to hold the coming image here.
lbl1 = Label(selectimage, bg = "black")
lbl1.place(x = -12, y = -12)

# creating the download image frame here.
downloadimage = Frame(canvas, width = 240, height = 230, bg = "black", relief = GROOVE, border=10)
downloadimage.place(x = 485, y = 165)
# creating the label to hold the coming image here.
lbl2 = Label(downloadimage, bg = "black")
lbl2.place(x = -12, y = -12)

window.mainloop()