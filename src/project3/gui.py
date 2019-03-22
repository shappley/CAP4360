import random
import tkFileDialog as filedialog
from Tkinter import *
from subprocess import Popen, PIPE

from attributes import Attributes, Attribute
from constraints import Constraint
from preference import Preference


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

    def append_results(self, value):
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

        self._attributes = Text(frame, width=50, borderwidth=2, relief=SOLID)
        self._attributes.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W + E)

        self._constraints = Text(frame, width=50, borderwidth=2, relief=SOLID)
        self._constraints.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky=W + E)

        self._preferences = Text(frame, width=50, borderwidth=2, relief=SOLID)
        self._preferences.grid(row=1, column=4, columnspan=2, padx=10, pady=10, sticky=W + E)

        self._results = Text(frame, width=50, borderwidth=2, relief=SOLID)
        self._results.grid(row=1, column=6, columnspan=2, padx=10, pady=10)

        frame.pack()
        root.mainloop()

    def generate_results(self):
        self.set_results("")
        print "generating results"
        try:
            # -------------------------------------------------------------------------------------------------- #
            print "parsing attributes"
            attributes = Attributes()
            for s in self.get_attributes().split("\n"):
                att = Attribute.parse(s)
                if att is not None:
                    attributes.add(att)
            if attributes.length() == 0:
                raise Exception("No valid Attributes found")
            # -------------------------------------------------------------------------------------------------- #
            print "parsing constraints"
            constraints = []
            for s in self.get_constraints().split("\n"):
                constraints.append(Constraint(s))
            clasp = "p cnf %s %s\n" % (attributes.length(), len(constraints))
            for c in constraints:
                parse = c.parse_to_clasp(attributes)
                if parse is not None and parse != "0":
                    clasp = clasp + parse + "\n"
            # -------------------------------------------------------------------------------------------------- #
            print "writing to file"
            self.write_to_file("clasp_in.txt", clasp)
            print "running clasp"
            results = self.run_clasp("clasp_in.txt")
            clasp_objects = self.get_objects_from_clasp(results)
            # -------------------------------------------------------------------------------------------------- #
            print "parsing preferences"
            preferences = []
            for p in self.get_preferences().split("\n"):
                p = p.strip()
                if p != "":
                    match = re.match("(?P<preference>[a-zA-Z\s]+)\s*,\s*(?P<penalty>\d+)", p)
                    if match is None:
                        raise Exception("Invalid Preference format")
                    pref = match.group("preference")
                    penalty = match.group("penalty")
                    preferences.append(Preference(pref, int(penalty)))
            # -------------------------------------------------------------------------------------------------- #
            print "calculating penalties"
            object_penalties = Preference.calculate_penalties(clasp_objects, attributes, preferences)
            exemplification = random.sample(object_penalties, 2)
            # -------------------------------------------------------------------------------------------------- #
            print "writing results"
            self.append_results("{:-^50}\n".format(""))
            self.append_results("{:^50}".format("FEASIBLE OBJECTS"))
            self.append_results("\n{:-^50}\n".format(""))
            self.append_results("There are " + str(len(clasp_objects)) + " feasible objects")

            if len(clasp_objects) == 0:
                return

            self.append_results("\n\n{:-^50}\n".format(""))
            self.append_results("{:^50}\n".format("EXEMPLIFICATION"))
            self.append_results("{:-^50}\n".format(""))
            self.append_results("[Object Values], Penalty Value\n")
            self.append_results("O1 = [" + attributes.from_clasp(exemplification[0][0]) + "], "
                                + str(exemplification[0][1]) + "\n")
            self.append_results("O2 = [" + attributes.from_clasp(exemplification[1][0]) + "], "
                                + str(exemplification[1][1]) + "\n")
            if exemplification[0][1] > exemplification[1][1]:
                self.append_results("O2 is strictly preferred to O1")
            elif exemplification[0][1] < exemplification[1][1]:
                self.append_results("O1 is strictly preferred to O2 ")
            else:
                self.append_results("O1 is equally preferred to O2")

            self.append_results("\n\n{:-^50}\n".format(""))
            self.append_results("{:^50}\n".format("OPTIMAL OBJECTS"))
            self.append_results("{:-^50}\n".format(""))
            object_penalties.sort(key=lambda e: e[1])
            best = object_penalties[0][1]
            for o in object_penalties:
                if o[1] == best:
                    self.append_results("[%s], %s\n" % (attributes.from_clasp(o[0]), o[1]))
        except Exception as ex:
            self.set_results(ex.message)

    def format_clasp_results(self, objects, attributes, preferences):
        if len(objects) == 0:
            return "No Feasible Objects"
        results = ""
        i = 1
        for s in objects:
            s = s.strip()
            results = results + str(i) + ". (" \
                      + str(Preference.calculate_penalty(s, attributes, preferences)) + ") " \
                      + attributes.from_clasp(s) + "\n"
            i = i + 1
        return results

    def get_objects_from_clasp(self, clasp):
        objects = []
        for s in clasp.split("\n"):
            if s.startswith("v"):
                objects.append(s[2:])
        return objects

    def write_to_file(self, filename, value):
        with open(filename, "w") as f:
            f.write(value)

    def run_clasp(self, filename):
        process = Popen(["clasp", "0", filename], stdout=PIPE, stderr=PIPE)
        out, err = process.communicate()
        return out


UserPreferencesGUI()
