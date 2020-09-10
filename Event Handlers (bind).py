# Event Handlers - Functions
# Event loop - executes code if event occurs
# - started with windows.mainloop()
# Event object - when event occurs, instance of a class that represents event is instantiated

import tkinter as tk

window = tk.Tk()


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


def handle_click(event):
    print("The button was clicked!")


button = tk.Button(text="Click me!")
button.pack()


button.bind("<Button-1>", handle_click)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()
