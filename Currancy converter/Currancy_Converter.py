from tkinter import mainloop, Tk, Label, Entry, Button, END, Text
import json
from urllib.request import urlopen
from datetime import datetime
import os

# --------------------------------------------------------------------------- #

class Conversion:
    def __init__(self,currancy1,currancy2,amount,result=0.0,rate=0.0):
        self.currancy1 = currancy1
        self.currancy2 = currancy2
        self.rate = rate
        self.amount = amount
        self.result = result

    def __str__(self):
        return f"""Conversion from {self.currancy1} to {self.currancy2}
Amount: {self.amount}
Rate: {"%.5f" % float(self.rate)}
Result: {"%.2f" % float(self.result)}
Date: {datetime.utcnow().date()}"""

# --------------------------------------------------------------------------- #

def get_data(conversion):
    try:
        url = "http://www.floatrates.com/daily/" + conversion.currancy1 + ".json"
        with urlopen(url) as response:
            source = response.read()

        data = json.loads(source)
        rate = data[conversion.currancy2]["rate"]
        conversion.result = (conversion.amount * float(rate))
        conversion.rate = rate

        return None
    except:
        return "One or both of your currancy codes are invalid"


def save_data(conversion):
    path = os.path.dirname(os.path.abspath(__file__)) + "\\conversion_logs.txt"
    with open(path, "r") as f:
        f_data = f.read()

    f_data += f"""
    
{str(conversion)}
"""

    with open(path, "w") as f:
        f.write(f_data)


def output(message):
    output_field = Text(window, width=30,height=6)
    output_field.grid(row=5,column=0)
    output_field.insert(END,message)


def display_message():
    C1 = C1_input.get().lower()
    C2 = C2_input.get().lower()
    amount = int(amount_input.get())
    conversion = Conversion(C1,C2,amount)
    error = get_data(conversion)

    if conversion.amount <= 0:
        error = "Invalid amount"

    if error:
        output(error)
    else:
        output(conversion)
        save_data(conversion)
    
# --------------------------------------------------------------------------- #

window = Tk()
window.title("Currancy Converter")
window.geometry("300x260")
window.configure(background='#b1dbe6')

Label(window, text="Currancy Converter", font="Times 20 bold", bg="#b1dbe6").grid(row=0, column=0)
Label(window, text="From:", font="Broadway 15", bg="#b1dbe6").grid(row=1, column=0)

C1_input = Entry(window, width=4)
C1_input.grid(row=1, column=1)

Label(window, text="To:", font="Broadway 15", bg="#b1dbe6").grid(row=2, column=0)

C2_input = Entry(window, width=4)
C2_input.grid(row=2, column=1)

Label(window, text="Amount:", font="Broadway 15", bg="#b1dbe6").grid(row=3, column=0)

amount_input = Entry(window, width=7)
amount_input.grid(row=3, column=1)

Button(window, text="Calculate", command=display_message, bg="black", fg="white").grid(row=4, column=0)

window.mainloop()
