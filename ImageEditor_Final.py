from tkinter import *
from PIL import ImageTk, Image, ImageOps, ImageEnhance, ImageFilter
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import os
import tkinter.font as font
import numpy as np

root = Tk()
root.title("Image Editor")
root.geometry("1920x1080")
root.config(bg="black")


# define functions
def open_func():
    global original_img, final_img, img_path
    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    original_img = Image.open(img_path)
    original_img.thumbnail((750, 750))
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def crop_func():
    global original_img, final_img, img_path, root_crop, x1_input, x2_input, y1_input, y2_input
    
    x1_val = x1_input.get()
    x2_val = x2_input.get()
    y1_val = y1_input.get()
    y2_val = y2_input.get()
    root_crop.destroy()
    
    original_img_arr = np.array(original_img)
    original_img_arr = original_img_arr[int(y1_val):int(y2_val),int(x1_val):int(x2_val)]
    original_img = Image.fromarray(original_img_arr)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def crop_area_func():
    global root_crop, x1_input, x2_input, y1_input, y2_input
    root_crop = Tk()
    root_crop.title("Crop Area")

    x1_label = Label(root_crop, text="Top Left x-coordinate")
    x1_label.grid(row=0,column=0)
    y1_label = Label(root_crop, text="Top Left y-coordinate")
    y1_label.grid(row=1,column=0)
    x2_label = Label(root_crop, text="Bottom Right x-coordinate")
    x2_label.grid(row=2,column=0)
    y2_label = Label(root_crop, text="Bottom Right y-coordinate")
    y2_label.grid(row=3,column=0)
    button = Button(root_crop, text="Crop", command=crop_func)
    button.grid(row=4,column=0)
    
    x1_input = Entry(root_crop)
    x1_input.grid(row=0,column=1)
    y1_input = Entry(root_crop)
    y1_input.grid(row=1,column=1)
    x2_input = Entry(root_crop)
    x2_input.grid(row=2,column=1)
    y2_input = Entry(root_crop)
    y2_input.grid(row=3,column=1)
    root_crop.mainloop()


def black_white_func():
    global original_img, final_img, img_path
    '''
    original_img = ImageOps.grayscale(original_img)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    '''
    original_img.thumbnail((750, 750))
    original_img_arr = np.array(original_img)
    grayscale_img = np.mean(original_img_arr, axis=2)
    w = grayscale_img.shape[1] 
    h = grayscale_img.shape[0]

    for i in range(h):
        for j in range(w):
            if grayscale_img[i][j] < 128:
                grayscale_img[i][j] = 0
            else:
                grayscale_img[i][j] = 255

    original_img = Image.fromarray(grayscale_img)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img
    

def invert_color_func():
    global original_img, final_img, img_path
    original_img.thumbnail((750, 750))
    original_img = ImageOps.invert(original_img)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def flip_hor_func():
    global original_img, final_img, img_path
    '''
    original_img = original_img.transpose(Image.FLIP_LEFT_RIGHT)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    '''
    original_img.thumbnail((750, 750))
    original_img_arr = np.array(original_img)
    w = original_img_arr.shape[1] 
    h = original_img_arr.shape[0]
    empty_img = np.zeros_like(original_img_arr)

    for i in range (h):
        for j in range (w):
            empty_img[i,j] = original_img_arr[i,w-j-1]

    original_img = Image.fromarray(empty_img)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img

    
def flip_ver_func():
    global original_img, final_img, img_path
    '''
    original_img = original_img.transpose(Image.FLIP_TOP_BOTTOM)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    '''
    original_img.thumbnail((750, 750))
    original_img_arr = np.array(original_img)
    w = original_img_arr.shape[1] 
    h = original_img_arr.shape[0]
    empty_img = np.zeros_like(original_img_arr)

    for i in range (h):
        for j in range (w):
            empty_img[i,j] = original_img_arr[h-i-1,j]
            
    original_img = Image.fromarray(empty_img)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img

    
def rotate_right_func():
    global original_img, final_img, img_path
    '''
    original_img = original_img.rotate(-90)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    '''
    original_img.thumbnail((750, 750))
    original_img_arr = np.array(original_img)
    w = original_img_arr.shape[1] 
    h = original_img_arr.shape[0]
    c = original_img_arr.shape[2]
    empty_img = np.zeros([w,h,c], dtype=np.uint8)

    for i in range (h):
        for j in range (w):
            empty_img[j,h-i-1] = original_img_arr[i,j]
    
    original_img = Image.fromarray(empty_img)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img
    
    
def rotate_left_func():
    global original_img, final_img, img_path
    '''
    original_img = original_img.rotate(90)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    '''
    original_img.thumbnail((750, 750))
    original_img_arr = np.array(original_img)
    w = original_img_arr.shape[1] 
    h = original_img_arr.shape[0]
    c = original_img_arr.shape[2]
    empty_img = np.zeros([w,h,c], dtype=np.uint8)

    for i in range(0,h):
        for j in range(0,w):
            empty_img[w-j-1,i] = original_img_arr[i,j]
    
    original_img = Image.fromarray(empty_img)
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def bright_func(event):
    global original_img, final_img, img_path, bright_img_2
    for i in range(0, bright_var.get()+100):
        original_img.thumbnail((750, 750))
        bright_img = ImageEnhance.Brightness(original_img)
        bright_img_2 = bright_img.enhance(i/100.0)
        final_img = ImageTk.PhotoImage(bright_img_2)
        img_canvas.create_image(500, 377, image=final_img)
        img_canvas.image=final_img

def bright_btn_func():
    global original_img, final_img, bright_img_2
    original_img = bright_img_2
    original_img.thumbnail((750, 750))
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def contrast_func(event):
    global original_img, final_img, img_path, contrast_img_2
    for i in range(0, contrast_var.get()+100):
        original_img.thumbnail((750, 750))
        contrast_img = ImageEnhance.Contrast(original_img)
        contrast_img_2 = contrast_img.enhance(i/100.0)
        final_img = ImageTk.PhotoImage(contrast_img_2)
        img_canvas.create_image(500, 377, image=final_img)
        img_canvas.image=final_img

def contrast_btn_func():
    global original_img, final_img, contrast_img_2
    original_img = contrast_img_2
    original_img.thumbnail((750, 750))
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def sharpness_func(event):
    global original_img, final_img, img_path, sharpness_img_2
    for i in range(0, sharpness_var.get()+100):
        original_img.thumbnail((750,750))
        sharpness_img = ImageEnhance.Sharpness(original_img)
        sharpness_img_2 = sharpness_img.enhance(i/100.0)
        final_img = ImageTk.PhotoImage(sharpness_img_2)
        img_canvas.create_image(500, 377, image=final_img)
        img_canvas.image=final_img


def sharpness_btn_func():
    global original_img, final_img, sharpness_img_2
    original_img = sharpness_img_2
    original_img.thumbnail((750, 750))
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def color_func(event):
    global original_img, final_img, img_path, color_img_2
    for i in range(0, color_var.get()+100):
        original_img.thumbnail((750,750))
        color_img = ImageEnhance.Color(original_img)
        color_img_2 = color_img.enhance(i/100.0)
        final_img = ImageTk.PhotoImage(color_img_2)
        img_canvas.create_image(500, 377, image=final_img)
        img_canvas.image=final_img


def color_btn_func():
    global original_img, final_img, color_img_2
    original_img = color_img_2
    original_img.thumbnail((750, 750))
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def blur_func(event):
    global original_img, final_img, img_path, blur_img
    for i in range(0, blur_var.get()+1):
        original_img.thumbnail((750,750))
        blur_img = original_img.filter(ImageFilter.BoxBlur(i))
        final_img = ImageTk.PhotoImage(blur_img)
        img_canvas.create_image(500, 377, image=final_img)
        img_canvas.image=final_img


def blur_btn_func():
    global original_img, final_img, img_path, blur_img
    original_img = blur_img
    original_img.thumbnail((750, 750))
    final_img = ImageTk.PhotoImage(original_img)
    img_canvas.create_image(500, 377, image=final_img)
    img_canvas.image=final_img


def save_func():
    global original_img, final_img, img_path
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("PNG file","*.png"),("JPG file","*.jpg")])
    original_img.save(file)
    root.destroy()


# Canvas for image and buttons

img_canvas = Canvas(root, width=1000, height=754, bg="#2B2B2B")
img_canvas.grid(row=0, column=0, padx=20, pady=20)

button_canvas = Canvas(root, width=450, height=754, bg="grey")
button_canvas.grid(row=0, column=1)


# Defining font size
myFont = font.Font(size=12) 


# Making buttons

open = Button(root, text="Open File", font=myFont, width=20, command=open_func, activebackground="#222222", activeforeground="white") 
open.place(x=1175, y=25)

crop_area = Button(root, text="Crop", font=myFont, width=20, command=crop_area_func, activebackground="#222222", activeforeground="white")
crop_area.place(x=1175, y=90)

#crop = Button(root, text="Crop", font=myFont, width=20)
#crop.place(x=1300, y=90)

black_white = Button(root, text="Black & White", font=myFont, width=20, command=black_white_func, activebackground="#222222", activeforeground="white") 
black_white.place(x=1175, y=150)

invert_color = Button(root, text="Invert Colors", font=myFont, width=20, command=invert_color_func, activebackground="#222222", activeforeground="white") 
invert_color.place(x=1175, y=210)

flip_hor = Button(root, text="Flip Horizontally", font=myFont, width=20, command=flip_hor_func, activebackground="#222222", activeforeground="white") 
flip_hor.place(x=1050, y=270)

flip_ver = Button(root, text="Flip Vertically", font=myFont, width=20, command=flip_ver_func, activebackground="#222222", activeforeground="white") 
flip_ver.place(x=1300, y=270)

rotate_right = Button(root, text="Rotate Right", font=myFont, width=20, command=rotate_right_func, activebackground="#222222", activeforeground="white") 
rotate_right.place(x=1050, y=330)

rotate_left = Button(root, text="Rotate Left", font=myFont, width=20, command=rotate_left_func, activebackground="#222222", activeforeground="white") 
rotate_left.place(x=1300, y=330)

save = Button(root, text="Save", font=myFont, width=20, command=save_func, activebackground="#222222", activeforeground="white")
save.place(x=1175, y=740)


# Making sliders
# Need to press the button after changing details to save

bright_button = Button(root, text="Adjust Brightness", font=myFont, width=20, command=bright_btn_func)
bright_button.place(x=1050, y=400)
bright_var = IntVar()
bright_scale = Scale(root, from_=-100, to=100, variable=bright_var, orient=HORIZONTAL, command=bright_func)
bright_scale.place(x=1340, y=390)

contrast_button = Button(root, text="Adjust Contrast", font=myFont, width=20, command=contrast_btn_func)
contrast_button.place(x=1050, y=460)
contrast_var = IntVar()
contrast_scale = Scale(root, from_=-100, to=100, variable=contrast_var, orient=HORIZONTAL, command=contrast_func)
contrast_scale.place(x=1340, y=450)

sharpness_button = Button(root, text="Adjust Sharpness", font=myFont, width=20, command=sharpness_btn_func)
sharpness_button.place(x=1050, y=520)
sharpness_var = IntVar()
sharpness_scale = Scale(root, from_=-100, to=100, variable=sharpness_var, orient=HORIZONTAL, command=sharpness_func)
sharpness_scale.place(x=1340, y=510)

color_button = Button(root, text="Adjust Color", font=myFont, width=20, command=color_btn_func)
color_button.place(x=1050, y=580)
color_var = IntVar()
color_scale = Scale(root, from_=-100, to=100, variable=color_var, orient=HORIZONTAL, command=color_func)
color_scale.place(x=1340, y=570)

blur_button = Button(root, text="Blur", font=myFont, width=20, command=blur_btn_func)
blur_button.place(x=1050, y=640)
blur_var = IntVar()
blur_scale = Scale(root, from_=0, to=5, variable=blur_var, orient=HORIZONTAL, command=blur_func)
blur_scale.place(x=1340, y=630)

root.mainloop()
