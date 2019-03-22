from clause import Clause


class Preference:
    def __init__(self, value, penalty):
        self._value = value
        self._penalty = penalty

    def value(self):
        return self._value

    def penalty(self):
        return self._penalty

    def to_clasp_clauses(self, attributes):
        val = self.value()
        clauses = val.split("AND")
        clasp_clauses = []
        for c in clauses:
            clause = Clause(c)
            clasp_clauses.append(clause.parse_clause_to_clasp(attributes))
        return clasp_clauses
