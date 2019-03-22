from clause import Clause


class Constraint:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self.value()

    def value(self):
        return self._value

    def parse_to_clasp(self, attributes):
        return Clause(self.value()).parse_clause_to_clasp(attributes)
