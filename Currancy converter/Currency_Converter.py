from tkinter import mainloop, Tk, Label, Entry, Button, END, Text
import json
from urllib.request import urlopen
from datetime import datetime
import os

# --------------------------------------------------------------------------- #

# class to store conversion data
class Conversion:
    # initialses an instance
    def __init__(self,currency1,currency2,amount,result=0.0,rate=0.0):
        self.currency1 = currency1
        self.currency2 = currency2
        self.rate = rate
        self.amount = amount
        self.result = result

    # determines the output when instance is called
    def __str__(self):
        return f"""Conversion from {self.currency1} to {self.currency2}
Amount: {self.amount}
Rate: {"%.5f" % float(self.rate)}
Result: {"%.2f" % float(self.result)}
Date: {datetime.utcnow().date()}"""

# --------------------------------------------------------------------------- #

def get_data(conversion):
    # try except to catch invalid inputs
    try:
        # gets exchane data for currency 1
        url = "http://www.floatrates.com/daily/" + conversion.currency1 + ".json"
        with urlopen(url) as response:
            source = response.read()

        # converts text from url into a python dictonary
        data = json.loads(source)
        # gets the rate of exchange and calculates the resulting amount
        conversion.rate = data[conversion.currency2]["rate"]
        conversion.result = (conversion.amount * float(conversion.rate))
        error_message = None
    except:
        error_message = "An error occured, please check internet and currency codes."
        
    return error_message


def save_data(conversion):
    # gets the path to the currant file
    path = os.path.dirname(os.path.abspath(__file__)) + "\\conversion_logs.txt"
    # reads the data from the text file
    with open(path, "r") as f:
        f_data = f.read()
    # adds the conversion data to the data from the file
    f_data +=f"""
    
{str(conversion)}
"""
    # writes the updated data to the text file
    with open(path, "w") as f:
        f.write(f_data)


def output(message):
    # outputs a message in a text field
    output_field = Text(window, width=30,height=6)
    output_field.grid(row=5,column=0)
    output_field.insert(END,message)


def display_message():
    # gets the data from inputs
    C1 = C1_input.get().lower()
    C2 = C2_input.get().lower()
    amount = int(amount_input.get())
    # creates instance of Conversion class using user inputs
    conversion = Conversion(C1,C2,amount)
    # gets the exchange rate data and catches any errors
    error = get_data(conversion)

    # checks if amount input is valid
    if conversion.amount <= 0:
        error = "Invalid amount"

    # outputs conversion data if no errors
    if error:
        output(error)
    else:
        output(conversion)
        save_data(conversion)
    
# --------------------------------------------------------------------------- #

def Main():
    # creates window and sets its attributes
    window = Tk()
    window.title("currency Converter")
    window.geometry("300x260")
    window.configure(background='#b1dbe6')

    # Heading label
    Label(window, text="currency Converter", font="Times 20 bold", bg="#b1dbe6").grid(row=0, column=0)
    Label(window, text="From:", font="Broadway 15", bg="#b1dbe6").grid(row=1, column=0)

    # input field for currency 1
    C1_input = Entry(window, width=4)
    C1_input.grid(row=1, column=1)

    Label(window, text="To:", font="Broadway 15", bg="#b1dbe6").grid(row=2, column=0)

    # input field for currency 2
    C2_input = Entry(window, width=4)
    C2_input.grid(row=2, column=1)

    Label(window, text="Amount:", font="Broadway 15", bg="#b1dbe6").grid(row=3, column=0)

    # input field for amount
    amount_input = Entry(window, width=7)
    amount_input.grid(row=3, column=1)

    # button to start convert
    Button(window, text="Calculate", command=display_message, bg="black", fg="white").grid(row=4, column=0)

    # keeps window up
    window.mainloop()
    
if __name__ == '__main__':
    Main()
