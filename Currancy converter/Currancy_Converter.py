from tkinter import mainloop, Tk, Label, Entry, Button, END, Text
import json
from urllib.request import urlopen


def get_data(amount, currancy1, currancy2):
    url = "http://www.floatrates.com/daily/" + currancy1 + ".json"
    with urlopen(url) as response:
        source = response.read()

    data = json.loads(source)
    rate = data[currancy2]["rate"]

    result = "Result: " + str((amount * float(rate)))
    rate = "Rate: " + str(rate)
    return result, rate


def display_message():
    currancy1 = (input1.get()).lower()
    currancy2 = (input2.get()).lower()


    if input3.get() == "":
        amount = 0
    else:
        amount = int(input3.get())

    message = ""
    message2 = ""
    error_message = ""
    if amount <= 0:
        error_message += "invalid amount "
    elif currancy1 == "":
        error_message += "Enter the first currancy  "
    elif currancy2 == "":
        error_message += "Enter the second currancy "


    if error_message == "":
        message, message2 = get_data(amount, currancy1, currancy2)

        output_message = Text(master=window, width=25, height=1)
        output_message.grid(row=5, column=0)

        output_message.insert(END, message)
        
        output_message2 = Text(master=window, width=25, height=1)
        output_message2.grid(row=6, column=0)

        output_message2.insert(END, message2)

        error_message += "Success"



            
    error_output = Text(master=window, width=25, height=1)
    error_output.grid(row=7, column=0)

    error_output.insert(END, error_message)
    

    

# --------------------------------------------------- #


window = Tk()

window.title("Currancy Converter")
window.geometry("300x220")
window.configure(background='#b1dbe6')
# window.config.background("grey")

Label(window, text="Currancy Converter", font="Times 20 bold", bg="#b1dbe6").grid(row=0, column=0)


Label(window, text="From:", font="Broadway 15", bg="#b1dbe6").grid(row=1, column=0)

input1 = Entry(window, width=4)
input1.grid(row=1, column=1)

Label(window, text="To:", font="Broadway 15", bg="#b1dbe6").grid(row=2, column=0)

input2 = Entry(window, width=4)
input2.grid(row=2, column=1)

Label(window, text="Amount:", font="Broadway 15", bg="#b1dbe6").grid(row=3, column=0)

input3 = Entry(window, width=7)
input3.grid(row=3, column=1)

Button(window, text="Calculate", command=display_message, bg="black", fg="white").grid(row=4, column=0)

window.mainloop()