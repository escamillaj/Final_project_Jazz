######################################################################
# Author: Jazmin Escamilla
# Username: escamillaj
#
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html

# Assignment: Final Project
# Purpose: Add shapes to canvas

######################################################################
# Acknowledgements:
#
# originally modified by Dr. Jan Pearce
#
#
######################################################################

import tkinter as tk

import random

class Art_Show:
    
    def __init__(self):
        """
        Initializer
        """
        self.master = tk.Tk()
        self.frame_canvas = tk.Frame(self.master, width=500, height=400)
        self.frame_canvas.pack(side="left")
        self.c = tk.Canvas(self.frame_canvas, width=1250, height=350, background= "white")
        
        
        self.c.pack()
        #Square button
        self.Square = tk.Button(self.frame_canvas, command = self.draw_square)
        self.Square.config(text = "Square")
        self.Square.pack()
        self.c.bind("<Key>", key)
        self.c.bind("<Square>", callback())
    
    
        # Rectangle Button
        self.Rectangle = tk.Button(self.frame_canvas, command = self.draw_rectangle())
        self.Rectangle.config(text= "Rectangle")
        self.Rectangle.pack()
        
        # Circle Button
        self.Circle = tk.Button(self.frame_canvas, command = self.draw_circle)
        self.Circle.config(text= "Circle")
        self.Circle.pack()
        
    def key(self, event):
        repr(event.chr)
        
    def callback(self, event):
        print("Clicked at", event.x, event.y)
        
    def draw_square(self, event):
        """
        
        :param x:
        :param y:
        :return:
        """
        #self.shape= #new shape, random image from self.image
    #    circle = tk.PhotoImage(file="Black Circle.gif" )
    #    self.c.create_image(100, 100,image= circle)
        
        #click event to keep track of which button clicked. To perform tkinter draw shape
        
        square = self.c.create_rectangle(event.x, event.y, event.x+10, event.y+10, fill= "black")
        self.frame_canvas.bind("<Square>", )
        
    def draw_circle(self):
        """
        
        :return:
        """
        
    def draw_line(self):
        """
        
        :return:
        """
        
        line = self.c.create_line(event.x, event.y, event.x+10, event.y+10)
        
    def draw_rectangle(self):
        """
        
        :return:
        """
        rectangle = self.c.create_rectangle(event.x, event.y, event.x+40, event.y+50)
        
    def draw_oval(self):
        """
        
        :return:
        """
        oval= self.c.create_oval(event.x, event.y, event.x+30, event.y+40)


def main():
    
    
    a = Art_Show()      # creates a new tkinter object
    a.c.mainloop()
  
main()

# What is new, tk.image   and tk canvas
