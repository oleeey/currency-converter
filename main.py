import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
c = CurrencyRates(force_decimal=True)

window = tk.Tk()
window.geometry("300x300")

title = tk.Label(text="Currency Converter", font=("Input", 20))
fromText = tk.Label(text="From", font=("Input", 10))
inputEntry = tk.Entry(width=15)
inputEntry.insert(0, 1)
inputEntry.configure(justify="center")
combo1 = ttk.Combobox(state="readonly", 
                      values=["EUR", "USD", "HUF", "GBP", "CAD", "JPY", "AUD", "CHF", "RUB", "CZK"],
                      width=5
                      )
combo1.set("EUR")
toText = tk.Label(text="To", font=("Input", 10))
outputEntry = tk.Label(width=15)
combo2 = ttk.Combobox(state="readonly",
                      values=["EUR", "USD", "HUF", "GBP", "CAD", "JPY", "AUD", "CHF", "RUB", "CZK"],
                      width=5
                      )
combo2.set("USD")

curr1 = combo1.get()
curr2 = combo2.get()
val = int(inputEntry.get())
exr = c.convert(curr1, curr2, val)
outputEntry.configure(text=exr)

title.grid(column=0, row=0)
fromText.grid(column=0, row=1)
inputEntry.grid(column=0, row=2)
combo1.grid(column=1, row=2)
toText.grid(column=0, row=3)
outputEntry.grid(column=0, row=4)
combo2.grid(column=1, row=4)

window.mainloop()




