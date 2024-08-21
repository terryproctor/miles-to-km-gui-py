from tkinter import *

window = Tk()
window.minsize(width=45, height=25)
window.title("Mile to km Converter")
window.config(padx=20, pady=10)

input = Entry()
input.config(width=20)
input.grid(row=0, column=1)

label_miles = Label()
label_miles["text"] = "Miles"
label_miles.grid(row=0, column=2)

equal_to = Label()
equal_to["text"] = "is equal to"
equal_to.grid(row=1, column=0)

km_amount = Label()
km_amount["text"] = "    "
km_amount.grid(row=1, column=1)


km_label = Label()
km_label["text"] = "Km"
km_label.grid(row=1, column=2)

def convert():
    miles_amount = float(input.get())
    km_amount["text"] = miles_amount * 1.0609344

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(row=2, column=1)


window.mainloop()