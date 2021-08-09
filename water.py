#!/usr/bin/python
"""
Created on Fri Jun 25 09:28:46 2021

@author: MitchellCaywood
"""

import tkinter as tk
from PIL import ImageTk, Image
import time
import os
import random

def main():
    
    while True:
        
        #This creates the main window of an application
        window = tk.Tk()
        window.title("DRINK MORE WATER")
        window.configure(background='grey')
        
        path = 'C://Users//MitchellCaywood//OneDrive - Critical Room Control//Documents//Python Scripts//Misc//Water'

        random_image = random.choice(os.listdir(path))
        
        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path+'//'+random_image))
        
        window.geometry(str(img.width())+"x"+str(img.height()))
        
        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(window, image = img)
        
        #The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side = "bottom", fill = "both", expand = "yes")

        #Start the GUI
        window.mainloop()
        
        # wait for 20 minutes after closing the window to start again
        time.sleep(20*60)
        
if __name__ == "__main__":
    main()