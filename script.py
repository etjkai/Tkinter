import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame(master=window)
frame_b = tk.Frame(master=window,
                   # Creates a border around frame
                   relief=tk.RAISED,
                   # Border must be > 1 for frame to take effect
                   borderwidth=3)
'''
List of Widgets
1) Label (lbl)
2) Button (btn)
3) Entry (ent)
    - .get() - retrieve text
    - .delete() - delete text 
    - .insert() - insert text
4) Text (txt)
    - .get() / delete() parameters
        <line number>.<position of a character on that line> - e.g. "1.5"
    - .insert()
        -- Insert text at position if already present
        -- Append text to line if character number > index of last character
    - tk.END for all text in box
5) Frame (frm)
'''
# Creating Label widget
label_a = tk.Label(
    # Which frame to assign this widget
    master=frame_a,
    text='I am in Frame A!',
    foreground='black',
    # Height & width are respective to the character: 0
    width=40,
    height=10,
    background='orange'
)
label_b = tk.Label(master=frame_b,
                   text="I am in Frame B!",
                   height=15)


# Adding widgets into frame
label_a.pack()
label_b.pack()

'''
Geometry Managers
[1] .pack()
- creates rectangular area (parcel) just tall/wide enough for widget
    - fills rest with blank space
- centers widget by default
[2] .place()
- may be difficult to manage
- not responsive to resizing
[3] .grid()
'''

# Add frame into window
frame_a.pack()
frame_b.pack(
    # fill - which direction frames should fill: tk.X - horizontal, tk.Y - vertical, tk.BOTH
    fill=tk.X,
    side=tk.LEFT
)

# Run Tkinter event loop - listening for events, until window it is called on is closed.
window.mainloop()

# Close the window
# window.destroy()
