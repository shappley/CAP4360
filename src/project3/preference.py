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

    @staticmethod
    def calculate_penalties(objects, attributes, preferences):
        penalties = []
        for o in objects:
            penalties.append([o, Preference.calculate_penalty(o, attributes, preferences)])
        return penalties

    @staticmethod
    def calculate_penalty(feasible_object, attributes, preferences):
        penalty = 0
        for p in preferences:
            clasp = p.to_clasp_clauses(attributes)
            if not Preference.__object_is_preferred(feasible_object, clasp):
                penalty = penalty + p.penalty()
        return penalty

    @staticmethod
    def __object_is_preferred(feasible_object, preference):
        for clause in preference:
            clause = clause[:-2]
            for item in clause.split(" "):
                if item in feasible_object and "-" + item not in feasible_object:
                    break
            else:
                return False
        return True
