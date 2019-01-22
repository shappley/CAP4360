class States:
    def __init__(self, states):
        self._states = states

    def report(self):
        print "--------------------------------------------------------------------------------------"
        print "%-16s%-16s%-12s%-10s  %-15s%s" % (
            "State Name", "Capital City",
            "State Abbr", "Population", "Region",
            "US House Seats"
        )
        print "--------------------------------------------------------------------------------------"
        for state in self._states:
            print "%-16s%-16s%-12s%10s  %-15s%7s" % (
                state.name, state.capital, state.abbr,
                "{:,}".format(state.population), state.region, state.seats
            )
