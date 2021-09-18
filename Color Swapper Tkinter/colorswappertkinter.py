from tkinter import *
from tkinter import colorchooser
from PIL import Image,ImageTk
import importlib
import colorswapper as cs
import numpy as np
import os
import random



class MainWindow():
	def __init__(self,main):
		
		self.canvas = Canvas(main,width
			=300,height=300,highlightthickness=0)
		self.canvas.configure(bg='#1a1624')
		self.canvas.grid(row=0,column=0)

		self.hue = 0

		self.last_image = random.choice(images_input)
		
		read_image = Image.open('input'+'/'+self.last_image).resize((300,300),Image.ANTIALIAS)
		print(self.last_image)
		arr = np.array(read_image)
		# HUE SHIFT
		read_image = Image.fromarray(cs.shift_hue(arr,self.hue), 'RGBA')
		self.image_to_show = ImageTk.PhotoImage(read_image)
		self.image_on_canvas = self.canvas.create_image(0,0,anchor=NW, image = self.image_to_show)
		
		if len(images_input) > 1:
			self.btn_random_image = Button(
					root,
					text = "Random Image",
					command = lambda: self.show_image(self.random_image()),
					bg = '#322552',
					fg = '#cab5ff',
					)
			self.btn_random_image.grid(row=1,column=0)

		self.btn_choose_color = Button(
				root,
				text = "Select your goal color",
				command = self.choose_color,
				bg = '#322552',
				fg = '#cab5ff',
				)
		self.btn_choose_color.grid(row=2,column=0)

		self.btn_convert_all = Button(
				root,
				text = "Convert all images",
				command = lambda: cs.convert(self.hue),
				bg = '#322552',
				fg = '#cab5ff',
				)
		self.btn_convert_all.grid(row=3,column=0)

	def show_image(self,image):
		read_image = Image.open('input'+'/'+image).resize((300,300),Image.ANTIALIAS)
		arr = np.array(read_image)
		# HUE SHIFT
		read_image = Image.fromarray(cs.shift_hue(arr,self.hue), 'RGBA')
		self.image_to_show = ImageTk.PhotoImage(read_image)
		print("Showing image: "+image)
		self.canvas.itemconfig(self.image_on_canvas,image = self.image_to_show)

	def choose_color(self):
		color_code = colorchooser.askcolor(title = "Choose color")
		self.hue = cs.rgb_to_hsv(np.array(color_code[0]))[0]
		self.show_image(self.last_image)
		# cs.convert(cs.rgb_to_hsv(np.array(color_code[0]))[0])

	def random_image(self):
		temp_image = random.choice(images_input)
		while temp_image == self.last_image:
			temp_image = random.choice(images_input)
		self.last_image = temp_image
		return self.last_image

	def show_random_image(self):
		canvas.itemconfig(root.image_on_canvas, image = random_image())


current = os.getcwd()
images_input = os.listdir(current+"/input")
root = Tk()
root.configure(background='#1a1624')
MainWindow(root)
root.mainloop()