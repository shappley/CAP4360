from Tkinter import *
import tkFileDialog as filedialog


class UserPreferencesGUI:
    def __init__(self):
        self._attributes = None
        self._preferences = None
        self._constraints = None
        self._results = None
        self.gui()

    def load_file(self, text):
        file_handler = filedialog.askopenfile(title="Select File")
        if file_handler is not None:
            text.delete(1.0, END)
            text.insert(END, file_handler.read())
            file_handler.close()

    def get_preferences(self):
        return self._preferences.get(1.0, END)

    def get_attributes(self):
        return self._attributes.get(1.0, END)

    def get_constraints(self):
        return self._constraints.get(1.0, END)

    def gui(self):
        root = Tk()
        root.title("CAP4630 Project 3: User Preferences")
        root.resizable(False, False)
        frame = Frame(root, padx=10, pady=10)

        Label(frame, text="Attributes", font="Consolas 11 bold").grid(row=0, column=0, sticky=W, padx=10)
        Button(frame, text="Load", command=lambda: self.load_file(self._attributes)) \
            .grid(row=0, column=1, sticky=E, padx=10)

        Label(frame, text="Constraints", font="Consolas 11 bold").grid(row=0, column=2, sticky=W, padx=10)
        Button(frame, text="Load", command=lambda: self.load_file(self._constraints)) \
            .grid(row=0, column=3, sticky=E, padx=10)

        Label(frame, text="Preferences", font="Consolas 11 bold").grid(row=0, column=4, sticky=W, padx=10)
        Button(frame, text="Load", command=lambda: self.load_file(self._preferences)) \
            .grid(row=0, column=5, sticky=E, padx=10)

        Label(frame, text="Results", font="Consolas 11 bold").grid(row=0, column=6, sticky=W, padx=10)
        Button(frame, text="Generate").grid(row=0, column=7, padx=10, pady=10, sticky=E)

        self._attributes = Text(frame, width=35, borderwidth=2, relief=SOLID)
        self._attributes.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W + E)

        self._constraints = Text(frame, width=35, borderwidth=2, relief=SOLID)
        self._constraints.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky=W + E)

        self._preferences = Text(frame, width=35, borderwidth=2, relief=SOLID)
        self._preferences.grid(row=1, column=4, columnspan=2, padx=10, pady=10, sticky=W + E)

        self._results = Text(frame, width=35, borderwidth=2, relief=SOLID)
        self._results.grid(row=1, column=6, columnspan=2, padx=10, pady=10)

        frame.pack()
        root.mainloop()