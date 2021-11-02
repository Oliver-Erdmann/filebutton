from tkinter import *
import random
from PIL import Image
from tkinter import ttk
from tkinter import filedialog as fd

root=Tk()

#tkinter window
root.geometry("300x300")

#image grab
def select_files():
    global my_image
    filetypes = (('image files', '*.jpg .png'),('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    my_image = Image.open(filename)
    loop_img(my_image)

# add the parameter my_image to your function
def loop_img(my_image):
    red_slide = red_slider.get()
    green_slide = green_slider.get()
    blue_slide = blue_slider.get()

    skip_lines = spin.get()
    skip_lines_int = int(skip_lines)

    skip_pixels = spin_2.get()
    skip_pixels_int = int(skip_pixels)

    rows = my_image.size[0]
    cols = my_image.size[1]

# open button
open_button = ttk.Button(root,text='Open Files',command=select_files)
open_button.grid(row=0, column=1)

def My_image():

    red_slide = red_slider.get()
    green_slide = green_slider.get()
    blue_slide = blue_slider.get()

    skip_lines = spin.get()
    skip_lines_int = int(skip_lines)

    skip_pixels = spin_2.get()
    skip_pixels_int = int(skip_pixels)

    rows = my_image.size[0]
    cols = my_image.size[1]

    rows = my_image.size[0]
    cols = my_image.size[1]
    px = my_image.load()

    for i in range(0, rows):
        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 5)

        if i % 2 == 0:
            start = 0
        else:
            start = 1

        for j in range(start, cols, skip_lines_int):
            red = random.randint(0, red_slide)
            green = random.randint(0, green_slide)
            blue = random.randint(0, blue_slide)
            px[i, j] = (red, green, blue)

    my_image.show()

#button
Glitch_it = Button(root, text='Glitch it', command=My_image)
Glitch_it.grid(row=1, column=1)

#rgb sliders
red_slider = Scale(root, from_=0, to_=255,orient=HORIZONTAL, background='red', fg='grey')
red_slider.grid(row=0, column= 0)
green_slider = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='green', fg='grey')
green_slider.grid(row=1, column= 0)
blue_slider = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background='blue', fg='grey')
blue_slider.grid(row= 2, column=0)

#spin box
spin = Spinbox(root, from_=1, to=10, width=3)
spin.grid(row=3, column=0)
spin_2 = Spinbox(root, from_=1, to=10, width=3)
spin_2.grid(row=4, column=0)


root.mainloop()