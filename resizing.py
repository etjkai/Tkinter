import tkinter as tk

window = tk.Tk()

for i in range(3):
    # weight:
    # If every column and row is given a weight of 1, then they all grow at the same rate.
    # If one column has a weight of 1 and another a weight of 2, then the second column expands at twice the rate of the first.

    # minsize: minimum size of the row height or column width in pixels - displays Label text w/o chopping off
    window.columnconfigure(i, weight=1,
                           minsize=75
                           )
    window.rowconfigure(i, weight=1,
                        minsize=50
                        )

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
