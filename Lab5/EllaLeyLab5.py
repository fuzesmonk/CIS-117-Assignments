#Write an app that converts kilometers to miles using a GUI

#Requirements:
#A text entry that prompts the user for a measurement in kilometers
#Two buttons, a covert and quit button

import tkinter as tK

class ConversionGUI:
    def __init__(self):
        self.main_window = tK.Tk()

        #Label widget
        self.label = tK.Label(self.main_window, text="Kilometer to Miles Conversion \n Enter distance in kilometers you wish to convert")

        self.label.pack()

        tK.mainloop()

    def UserEntry(self):
        self.Entry = tK.Entry(self.main_window)
        self.Entry = float(self.Entry)


gui = ConversionGUI()
gui.UserEntry()
