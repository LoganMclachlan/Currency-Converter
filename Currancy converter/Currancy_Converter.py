from tkinter import mainloop, Tk, Label, Entry, Button, END, Text
import json
from urllib.request import urlopen

# opens the url depending on what the user inputed
def get_data(amount, currancy1, currancy2):
    url = "http://www.floatrates.com/daily/" + currancy1 + ".json"
    with urlopen(url) as response:
        source = response.read()

    # puts the data into the data variable
    data = json.loads(source)
    # finds the rate of the currency inputed
    rate = data[currancy2]["rate"]

    # uses the rate from data the program converts the amount inputed
    result = "Result: " + str((amount * float(rate)))
    rate = "Rate: " + str(rate)
    # returns the rate and amount converted
    return result, rate


def display_message():
    # gets the users input and converts it to lower case
    currancy1 = (input1.get()).lower()
    currancy2 = (input2.get()).lower()


    # amount is set to 1 if the user doesnt input an amount
    if input3.get() == "":
        amount = 1
    else:
        amount = int(input3.get())

    # initialises the output messages
    message = ""
    message2 = ""
    error_message = ""
    
    # validates the users input
    if amount <= 0:
        error_message += "invalid amount "
    elif currancy1 == "":
        error_message += "Enter the first currancy  "
    elif currancy2 == "":
        error_message += "Enter the second currancy "


    # will calculate the amount if no errors are found
    if error_message == "":
        # puts the converted amount into message 1 and the rate into message 2
        message, message2 = get_data(amount, currancy1, currancy2)

        # creates output field for the colculated amount
        output_message = Text(master=window, width=25, height=1)
        output_message.grid(row=5, column=0)

        output_message.insert(END, message)
        
        # creates output field for the rate of conversion
        output_message2 = Text(master=window, width=25, height=1)
        output_message2.grid(row=6, column=0)

        output_message2.insert(END, message2)

        # lets user know that the conversion was succesfull
        error_message += "Success"



    # outputs an errors
    error_output = Text(master=window, width=25, height=1)
    error_output.grid(row=7, column=0)

    error_output.insert(END, error_message)
    

    

# --------------------------------------------------- #

# creates window
window = Tk()

# sets the windows atributes
window.title("Currancy Converter")
window.geometry("300x220")
window.configure(background='#b1dbe6')# sets background color to a light blue

# displays the title on thw window
Label(window, text="Currancy Converter", font="Times 20 bold", bg="#b1dbe6").grid(row=0, column=0)


Label(window, text="From:", font="Broadway 15", bg="#b1dbe6").grid(row=1, column=0)

# creates input field for currency 1
input1 = Entry(window, width=4)
input1.grid(row=1, column=1)

Label(window, text="To:", font="Broadway 15", bg="#b1dbe6").grid(row=2, column=0)

# creates input field for currency 2
input2 = Entry(window, width=4)
input2.grid(row=2, column=1)

Label(window, text="Amount:", font="Broadway 15", bg="#b1dbe6").grid(row=3, column=0)

# creates input field for amount
input3 = Entry(window, width=7)
input3.grid(row=3, column=1)

# creates button to calculate amount
Button(window, text="Calculate", command=display_message, bg="black", fg="white").grid(row=4, column=0)

window.mainloop()
