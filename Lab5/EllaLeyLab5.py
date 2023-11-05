import tkinter as tk
from tkinter import messagebox


def exitProgram():
    mainWindow.destroy()


mainWindow = tk.Tk()
mainWindow.title("Kilometers to Miles Converter")

mainWindow.geometry("300x300")

instructionsLabel = tk.Label(mainWindow, text="Enter value(in kilometers) you wish to convert")
instructionsLabel.pack()

kiloEntry = tk.Entry(mainWindow)
kiloEntry.pack()

def convert_to_miles():
    try:
        kilometers = float(kiloEntry.get())
        miles = kilometers * 0.621371
        ConvertedValue.config(text=f"{kilometers} kilometers is {miles:.2f} miles")
    except ValueError:
        messagebox.showerror("Error, input a valid number for kilometers")

ConversionButton = tk.Button(mainWindow, text="Convert", command=convert_to_miles)
ConversionButton.pack()
ExitButton = tk.Button(mainWindow, text="Quit", command=exitProgram)
ExitButton.pack()

ConvertedValue = tk.Label(mainWindow, text="")
ConvertedValue.pack()

mainWindow.mainloop()

