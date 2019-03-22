import re


class Attribute:
    def __init__(self, name, values):
        self._name = name
        self._values = values

    def __str__(self):
        return "%s: %s" % (self._name, self._values)

    def name(self):
        return self._name

    def values(self):
        return self._values

    @staticmethod
    def parse(value):
        match = re.search("^(?P<name>[\w-]+):\s*(?P<valuea>[\w-]+),\s*(?P<valueb>[\w-]+)$", value)
        if match is not None:
            name = match.group("name")
            valuea = match.group("valuea")
            valueb = match.group("valueb")
            if name and valuea and valueb:
                return Attribute(name, [valuea, valueb])
        return None


class Attributes:
    def __init__(self):
        self._attributes = []

    def add(self, value):
        self._attributes.append(value)

    def index_of(self, value):
        return next((i for i, v in enumerate(self._attributes) if v == value), -1)

    def index_of_value(self, value):
        return next((i for i, v in enumerate(self._attributes) if value in v.values()), -1)

    def to_clasp_value(self, value):
        index = self.index_of_value(value)
        if index == -1:
            return None
        index = index + 1
        if self._attributes[index - 1].values()[1] == value:
            index = -index
        return index

    def from_clasp(self, value):
        res = ""
        for s in value.strip()[:-2].split(" "):
            val = int(s)
            val_index = 0
            if val < 0:
                val_index = 1
            res = res + self.get_attributes()[abs(val) - 1].values()[val_index] + ", "
        return res[:-2]

    def contains(self, value):
        return self.index_of(value) != -1

    def length(self):
        return len(self._attributes)

    def get_attributes(self):
        return self._attributes
