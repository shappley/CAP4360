import Sort
import Search


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
        self._sorted_by_name = False

    def search_by_name(self, name):
        i = Search.binary_search(self._states, name.lower(), key=lambda k: k.name.lower()) \
            if self._sorted_by_name \
            else Search.sequential_search(self._states, name.lower(), key=lambda k: k.name.lower())
        if i == -1:
            return None
        else:
            return self._states[i]
