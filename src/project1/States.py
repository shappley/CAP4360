import Sort


class States:
    def __init__(self, states):
        self._states = states
        self._sorted_by_name = False

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

    def sort_by_name(self):
        Sort.quicksort(array=self._states, key=lambda k: k.name)
        self._sorted_by_name = True

    def sort_by_population(self):
        Sort.radix_sort(self._states, key=lambda k: k.population)
