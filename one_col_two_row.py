import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1, 2], minsize=100)

label0 = tk.Button(text="AAAAAA", bg='white')
# Filling entire cell (NS vertical, EW horizontal)
label0.grid(row=0, column=0, sticky='nse')

label1 = tk.Button(text="AAAAAA", bg='red')
label1.grid(row=0, column=0, sticky='n')

label2 = tk.Button(text="BBBBB", bg='orange')
label2.grid(row=1, column=0, sticky='s')

label3 = tk.Button(text="BBBBB", bg='purple')
label3.grid(row=1, column=0, sticky='w')


label4 = tk.Button(text="BBBBB", bg='pink')
# Fill entire cell
label4.grid(row=2, column=0, sticky='nsew')


window.mainloop()
