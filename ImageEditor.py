from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.title("Image Editor")
#root.icon()
root.geometry("1920x1080")
root.config(bg="black")

#img_frame = LabelFrame(root, bg="black", borderwidth=0)
#img_frame.grid(row=0, column=0)

img_canvas = Canvas(root, width=1000, height=754, bg="white")
img_canvas.grid(row=0, column=0, padx=20, pady=20)

#cmds_frame = LabelFrame(root, borderwidth=0)
#cmds_frame.grid(row=0, column=1)

myFont = font.Font(size=12) #Defining font size

open = Button(root, text="Open File", font=myFont, width=20) #Add command
open.place(x=1175, y=20)

crop_area = Button(root, text="Select area to crop", font=myFont, width=20) #Add command
crop_area.place(x=1050, y=90)

crop = Button(root, text="Crop", font=myFont, width=20) #Add command
crop.place(x=1300, y=90)

black_white = Button(root, text="Black & White", font=myFont, width=20) #Add command
black_white.place(x=1175, y=150)

invert_color = Button(root, text="Invert Colors", font=myFont, width=20) #Add command
invert_color.place(x=1175, y=210)

flip_hor = Button(root, text="Flip Horizontally", font=myFont, width=20) #Add command
flip_hor.place(x=1050, y=270)

flip_ver = Button(root, text="Flip Vertically", font=myFont, width=20) #Add command
flip_ver.place(x=1300, y=270)

rotate_right = Button(root, text="Rotate Right", font=myFont, width=20) #Add command
rotate_right.place(x=1050, y=330)

rotate_left = Button(root, text="Rotate Left", font=myFont, width=20) #Add command
rotate_left.place(x=1300, y=330)

save = Button(root, text="Save", font=myFont, width=20) #Add command
save.place(x=1175, y=745)

root.mainloop()