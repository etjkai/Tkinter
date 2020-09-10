# Grid splits window/Frame into rows & columns

import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        # .grid() Geometry Manager applies to window object
        # attaches the grid to Window, with following coordinates
        frame.grid(row=i, column=j, padx=5, pady=15)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")

        # Label attached to Frame
        # Padding around the label
        label.pack(padx=15, pady=15)

window.mainloop()
