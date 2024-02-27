import tkinter as tk

def on_button_click(value):
    current = entry_var.get()
    entry_var.set(current + value)

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except:
        entry_var.set("Error")

root = tk.Tk()
root.title("Калькулятор")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=7, height=4, command=lambda value=button_text: on_button_click(value))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(root, text="C", width=7, height=4, command=clear)
clear_button.grid(row=5, column=0)

calculate_button = tk.Button(root, text="=", width=24, height=4, command=calculate)
calculate_button.grid(row=5, column=1, columnspan=3)


root.mainloop()