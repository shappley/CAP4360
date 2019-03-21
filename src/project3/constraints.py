import re


class Constraint:
    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def parse_to_clasp(self, attributes):
        clasp = ""
        value = self.value()
        while len(value) > 0:
            match = re.match("(?P<negation>NOT\s*)?(?P<item>\w+)(?P<separator>\s*OR\s*)?", value)
            negation = match.group("negation")
            item = match.group("item")
            separator = match.group("separator")
            count = 0
            if item is None:
                raise Exception("Invalid Constraints format")
            count = count + len(item)
            index = attributes.to_clasp_value(item)
            if index is None:
                raise Exception("Unknown Attribute %s" % item)
            if negation is not None:
                count = count + len(negation)
                index = -index
            if separator is not None:
                count = count + len(separator)
            clasp = clasp + str(index) + " "
            value = value[count:]
        return clasp + "0"
