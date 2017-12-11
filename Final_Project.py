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
        self.frame_canvas = tk.Frame(self.master, width=400, height=400)
        self.frame_canvas.config(bg="light blue")
     #   self.frame_canvas.winfo_geometry('400x200+100+50')
     #   self.frame_canvas.title("Art Show")
     #   self.frame_canvas.resizable(width=False, height=False)
        self.frame_canvas.pack(side="left")
        self.c = tk.Canvas(self.frame_canvas, width=400, height=350, background= "white")
        self.c.pack(side="right")
        
        #Square button
        self.Square = tk.Button(self.frame_canvas, command = self.draw_square)
        self.Square.config(text = "Square")
        self.Square.pack(side="left")

    
        # Rectangle Button
        self.Rectangle = tk.Button(self.frame_canvas, command= self.draw_rectangle())
        self.Rectangle.config(text= "Rectangle")
        self.Rectangle.pack(side="left")
        
        # Circle Button
        self.Circle = tk.Button(self.frame_canvas, command= self.draw_circle)
        self.Circle.config(text= "Circle")
        self.Circle.pack(side="left")
        
        # Oval Button
        self.Oval = tk.Button(self.frame_canvas, command = self.draw_oval)
        self.Oval.config(text= "Oval")
        self.Oval.pack(side="left")
        
        # Line Button
        self.Line = tk.Button(self.frame_canvas, command= self.draw_line)
        self.Line.config(text="Line")
        self.Line.pack(side="left")
        
        # Clear Canvas
        self.Delete_Canvas = tk.Button(self.frame_canvas. command= self.Clear_Canvas)
        
    def current_shape(self):
        """
        
        :return:
        """
        global current_shape
        current_shape = self.c.create_rectangle(20, 20, 40, 20, fill="Blue", outline="black")
    
    def click(self, event):
        global current_shape
        if current_shape is not None:
            cord = self.c.coords(current_shape)
            width = cord[2]-cord[0]
            height = cord[3]-cord[1]
            self.c.coords(current_shape,event.x, event.y, event.x+10, event.y+10 )
 
        
    def draw_square(self):

        #click event to keep track of which button clicked. To perform tkinter draw shape
        global current_shape
        current_shape = self.c.create_rectangle(20, 20, 70, 20, fill= "black", width=3)

        
    def draw_circle(self):
        global current_shape
        current_shape = self.c.create_oval(10, 10, 40, 40, fill="blue", width= 3)
        
    def draw_line(self):
        global current_shape
        current_shape = self.c.create_line(100, 1000, 300, 300, fill="black", widt= 5)
        
    def draw_rectangle(self):
        global current_shape
        self.c.create_rectangle(30, 30, 60, 30, fill="black", width= 3)
        
    def draw_oval(self):
        global current_shape
        current_shape = self.c.create_oval(10, 10, 70, 70, fill= "black", width= 3)

# Eraser to clear Canvas
# Drag object clicked
# Textbox to type into canvas.


def main():
    a = Art_Show()      # creates a new tkinter object
    a.c.mainloop()
  
main()

# What is new, tk.image   and tk canvas
