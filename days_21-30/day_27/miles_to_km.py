import tkinter


def calculate():
    miles_data = float(input.get())
    km_data = round(miles_data * 1.60934, 2)
    km_result_label.config(text=f"{km_data}")


window = tkinter.Tk()
window.title("Miles To Kilometers Converter")
window.config(padx=20, pady=20)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_label = tkinter.Label(text="miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

km_result_label = tkinter.Label(text=0)
km_result_label.grid(column=1, row=1)

input = tkinter.Entry(width=8)
input.insert(index=2, string="0")
input.grid(column=1, row=0)

calc_button = tkinter.Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)
window.mainloop()
