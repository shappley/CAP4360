import Sort
import Search

"""
A class for manipulating a collection of States
"""


class States:
    def __init__(self, states):
        self._states = states
        self._sorted_by_name = False

    def report(self):
        """
        Prints a formatted report of states
        """
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
        """
        Sorts the array of states by name
        """
        Sort.quicksort(array=self._states, key=lambda k: k.name)
        self._sorted_by_name = True

    def sort_by_population(self):
        """
        Sorts the array of states by population
        """
        Sort.radix_sort(self._states, key=lambda k: k.population)
        self._sorted_by_name = False

    def search_by_name(self, name):
        """
        Searches the array by state name.
        If the array is sorted by name, uses Binary Search.
        Sequential search otherwise.
        :param name: The name of the state to search for
        :return: The state matching the name if found, None otherwise.
        """
        i = Search.binary_search(self._states, name.lower(), key=lambda k: k.name.lower()) \
            if self._sorted_by_name \
            else Search.sequential_search(self._states, name.lower(), key=lambda k: k.name.lower())
        if i == -1:
            return None
        else:
            return self._states[i]
