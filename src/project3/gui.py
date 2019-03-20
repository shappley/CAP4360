from Tkinter import *
import tkFileDialog as filedialog


def load_file(text):
    text.delete(1.0, END)
    with filedialog.askopenfile(title="Select File") as file_handler:
        text.insert(END, file_handler.read())


def gui():
    root = Tk()
    root.title("CAP4630 Project 3: User Preferences")
    frame = Frame(root, padx=10, pady=10)

    attributes_label = Label(frame, text="Attributes", font="Consolas 11 bold") \
        .grid(row=0, column=0, sticky=W, padx=10)
    add_attributes = Button(frame, text="Load", command=lambda: load_file(attributes)) \
        .grid(row=0, column=1, sticky=E, padx=10)

    constraints_label = Label(frame, text="Constraints", font="Consolas 11 bold") \
        .grid(row=0, column=2, sticky=W, padx=10)
    add_constraints = Button(frame, text="Load", command=lambda: load_file(constraints)) \
        .grid(row=0, column=3, sticky=E, padx=10)

    preferences_label = Label(frame, text="Preferences", font="Consolas 11 bold") \
        .grid(row=0, column=4, sticky=W, padx=10)
    add_preferences = Button(frame, text="Load", command=lambda: load_file(preferences)) \
        .grid(row=0, column=5, sticky=E, padx=10)

    attributes = Text(frame, width=35, borderwidth=2, relief=SOLID)
    attributes.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    constraints = Text(frame, width=35, borderwidth=2, relief=SOLID)
    constraints.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

    preferences = Text(frame, width=35, borderwidth=2, relief=SOLID)
    preferences.grid(row=1, column=4, columnspan=2, padx=10, pady=10)

    frame.pack()
    root.mainloop()


gui()
