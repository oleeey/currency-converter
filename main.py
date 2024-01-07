import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

c = CurrencyRates(force_decimal=True)

cList = ["EUR", "USD", "HUF", "GBP", "CAD", "JPY", "AUD", "CHF", "CZK"]

cRates = {}

print("Importing exchange rates...")

for curr in cList:
    currList = []
    for curr2 in cList:
        currList.append(c.get_rate(curr, curr2))
    cRates[curr] = currList

print("Done!")

def convCurr(curr1, curr2, num):
    return round(num * cRates[curr1][cList.index(curr2)], 2)

win = tk.Tk()
win.title("Currency Converter")
win.geometry("300x300")

title = tk.Label(win, text="Currency Converter", font=("Input", 25))
fromText = tk.Label(win, text="From", font=("Input", 15))

myvar = tk.StringVar()
myvar2 = tk.StringVar()
myvar3 = tk.StringVar()
myvar.set('')
myvar2.set('')
myvar3.set('')

inputEntry = tk.Entry(win, width=15, textvariable=myvar, font=("Input", 10), justify="center")
inputEntry.insert(0, 1)

combo1 = ttk.Combobox(win, state="readonly",
                      justify="center",
                      values=cList,
                      width=10,
                      textvariable=myvar2
                      )
combo1.set("EUR")
toText = tk.Label(win, text="To", font=("Input", 15))
outputEntry = tk.Label(win, width=13, font=("Input", 10))
outputEntry.configure(background="#E3E3E3")
combo2 = ttk.Combobox(win, state="readonly",
                      justify="center",
                      values=cList,
                      width=10,
                      textvariable=myvar3
                      )
combo2.set("USD")

lbAuthor = tk.Label(win, text="Oliver Giczi")

def cback(x=1, y=1, z=1):
    try:
        num = int(inputEntry.get())
    except ValueError:
        print("Invalid input!")
        num = 0

    exr = convCurr(combo1.get(), combo2.get(), num)
    outputEntry.configure(text=exr)

myvar.trace('w', cback)
myvar2.trace('w', cback)
myvar3.trace('w', cback)

title.place(relx=0.5, rely= 0.1, anchor="center")
fromText.place(relx=0.5, rely= 0.3, anchor="center")
inputEntry.place(relx=0.35, rely= 0.4, anchor="center")
combo1.place(relx=0.7, rely= 0.4, anchor="center")
toText.place(relx=0.5, rely= 0.5, anchor="center")
outputEntry.place(relx=0.35, rely= 0.6, anchor="center")
combo2.place(relx=0.7, rely= 0.6, anchor="center")
lbAuthor.place(relx=0.5, rely=0.94, anchor="center")

cback()

win.mainloop()




