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
        
 #       self.Button1.pack()
 #       self.current_shape= tk.image()

        self.master = tk.Tk()
        frame_canvas = tk.Frame(self.master, width=500, height=400)
        frame_canvas.pack(padx=50, pady=50)
        self.c = tk.Canvas(frame_canvas, width=1250, height=350, background= "white")
        self.c.pack()
        self.Button1 = tk.Button(frame_canvas, command = self.draw_shape)
        self.Button1.config(text = "Random Shape")
        self.Button1.pack(padx= 20, pady=30)
        self.Button2 = tk.Button(frame_canvas, command = self.draw_shape)
        self.Button2.config(text= "Scenery")
        self.Button2.pack()
        
    
        
        
    def button_handler(self):
        """
        
        :return:
        """
        
    
    def draw_shape(self):
        """
        
        :param x:
        :param y:
        :return:
        """
        #self.shape= #new shape, random image from self.image
        circle = tk.PhotoImage(file="Black Circle.gif" )
        self.c.create_image(100, 100,image= circle)
        self.c.create_rectangle(10, 10, 30, 10, fill= "black")
        self.c.create_line(15, 25, 200, 25)
    
    def change_shape(self):
        """
        
        :return:
        """
        # new shape and random pick from self.images

def main():

    a = Art_Show()      # creates a new tkinter object
    a.c.mainloop()
  
main()

# What is new, tk.image   and tk canvas
