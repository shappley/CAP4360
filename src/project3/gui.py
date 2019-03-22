import tkFileDialog as filedialog
from Tkinter import *
from subprocess import Popen, PIPE

from attributes import Attributes, Attribute
from constraints import Constraint


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

    def set_results(self, value):
        self._results.delete(1.0, END)
        self._results.insert(END, value)

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
        Button(frame, text="Generate", command=self.generate_results).grid(row=0, column=7, padx=10, pady=10, sticky=E)

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

    def generate_results(self):
        print "generating results"
        try:
            attributes = Attributes()
            print "parsing attributes"
            for s in self.get_attributes().split("\n"):
                att = Attribute.parse(s)
                if att is not None:
                    attributes.add(att)
            if attributes.length() == 0:
                raise Exception("No valid Attributes found")
            constraints = []
            print "parsing constraints"
            for s in self.get_constraints().split("\n"):
                c = Constraint(s)
                constraints.append(c)
            clasp = "p cnf %s %s\n" % (attributes.length(), len(constraints))
            print clasp
            for c in constraints:
                parse = c.parse_to_clasp(attributes)
                if parse != "0":
                    clasp = clasp + parse + "\n"
            print "writing to file"
            self.write_to_file("clasp_in.txt", clasp)
            print "running clasp"
            results = self.run_clasp("clasp_in.txt")
            print results
            self.set_results(results)
        except Exception as ex:
            self.set_results(ex.message)

    def write_to_file(self, filename, value):
        with open(filename, "w") as f:
            f.write(value)

    def run_clasp(self, filename):
        process = Popen(["clasp", "0", filename], stdout=PIPE, stderr=PIPE)
        out, err = process.communicate()
        return out


UserPreferencesGUI()
