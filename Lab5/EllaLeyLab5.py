#Write an app that converts kilometers to miles using a GUI

#Requirements:
#A text entry that prompts the user for a measurement in kilometers
#Two buttons, a covert and quit button

import tkinter as tK

class ConversionGUI:

    def exitButton(self):
        exit()
    def __init__(self):
        self.main_window = tK.Tk()
        self.main_window.geometry("300x300")
        #Label widget
        self.label = tK.Label(self.main_window, text="Kilometer to Miles Conversion \n "
                                                     "Enter distance in kilometers you wish to convert")
        self.label.pack()

        #Entry Field
        self.entry = tK.Entry(self.main_window)
        self.entry.pack()

        def conversion(entry):
            entry = float(entry)
            #kilometer to meter
            MeterConversion = (entry) * 1000
            #meters to miles
            MilesConversion = MeterConversion / 1609.344
        ConversionButton = tK.Button(self.main_window,
                                     text="Click to Convert from Kilometers to Miles",
                                     command=ConversionGUI.__init__(conversion(self.entry)))
        ConversionButton.pack()



        #Exit Button
        exitButton = tK.Button(self.main_window, text="Click to exit", command=ConversionGUI.exitButton)
        exitButton.place(x=156, y=200)

        tK.mainloop()


gui = ConversionGUI()


