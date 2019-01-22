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
        self._quicksort(self._states, 0, len(self._states) - 1)
        self._sorted_by_name = True

    def _quicksort(self, array, lo, hi):
        if lo < hi:
            p = self._partition(array, lo, hi)
            self._quicksort(array, lo, p - 1)
            self._quicksort(array, p + 1, hi)

    def _partition(self, array, lo, hi):
        pivot = array[hi]
        i = lo
        for j in range(lo, hi):
            if array[j].name < pivot.name:
                self._swap(array, i, j)
                i += 1
        self._swap(array, i, hi)
        return i

    def _swap(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
