import re


class Clause:
    def __init__(self, value):
        self._value = value

    def parse_clause_to_clasp(self, attributes):
        clasp = ""
        disjunctions = self._value.split("OR")
        for c in disjunctions:
            c = c.strip()
            match = re.match("(?P<neg>NOT\s*)?(?P<att>[\w-]+)", c)
            if match is None:
                return None
            att = match.group("att")
            index = attributes.to_clasp_value(att)
            if index is None:
                raise Exception("Unknown Attribute %s" % att)
            if match.group("neg") is not None:
                index = -index
            clasp = clasp + str(index) + " "
        return clasp + "0"
