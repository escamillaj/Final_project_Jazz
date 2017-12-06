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

class Art_Show:
    def __init__(self):
        """
        Initializer
        """
        self.wn = tk()
        self.canvas = tk.canvas  #.. command= draw_shape)
  #      self.button = TK.button1
        self.current_shape= tk.image()
        
    def draw_shape(self,x,y):
        #self.shape= #new shape, random image from self.image
    
    def change_shape(self):
        # new shape and random pick from self.images

def main():
    a = Art_Show()
    
# What is new, tk.image   and tk canvas
