#Write an app that converts kilometers to miles using a GUI

#Requirements:
#A text entry that prompts the user for a measurement in kilometers
#Two buttons, a covert and quit button

import tkinter as tK

class ConversionGUI:

    def conversion(self):
        entry = float(self)
        # kilometer to meter
        MeterConversion = (entry) * 1000
        # meters to miles
        MilesConversion = MeterConversion / 1609.344

    def __init__(self):
        self.main_window = tK.Tk()
        self.main_window.geometry("300x300")
        #Label widget
        self.label = tK.Label(self.main_window, text="Kilometer to Miles Conversion \n "
                                                     "Enter distance in kilometers you wish to convert")
        self.label.pack()

        #Entry Field
        self.entry = tK.Entry(self.main_window)
        KilometerValue = self.entry.get()
        self.entry.pack()

        #Conversion Button
        conButton = tK.Button(self.main_window, text="Click to Convert",
                                command=ConversionGUI.conversion)
        conButton.place(x=50, y=200)

        #Exit Button
        exitButton = tK.Button(self.main_window, text="Click to exit", command=self.main_window.destroy)
        exitButton.place(x=156, y=200)

        tK.mainloop()


gui = ConversionGUI()


