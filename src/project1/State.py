class State:
    """
    Representation of a State, containing its name, capital,
    two-letter abbreviation, population, region, and US House Seats
    """

    def __init__(self, name, capital, abbr, population, region, seats):
        """
        Creates a State
        :param name: The name of the State (e.g. Florida)
        :param capital: The capital city of the State (e.g. Tallahassee)
        :param abbr: The two-letter abbreviation (e.g. FL)
        :param population: The population of the State
        :param region: The region of the US where the state resides
        :param seats: The number of US House Representative Seats for this State
        """
        self._seats = seats
        self._region = region
        self._population = population
        self._abbr = abbr
        self._capital = capital
        self._name = name

    @property
    def name(self):
        """
        :return: the state name
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        sets the state name to the specified value
        :param value the new name of the state
        """
        self._name = value

    @property
    def capital(self):
        """
        :return: the state capital city
        """
        return self._capital

    @capital.setter
    def capital(self, value):
        """
        sets the state capital to the specified value
        :param value the new capital of the state
        """
        self._capital = value

    @property
    def abbr(self):
        """
        :return: the state abbreviation
        """
        return self._abbr

    @abbr.setter
    def abbr(self, value):
        """
        sets the state name to the specified value
        :param value the new name of the state
        """
        self._abbr = value

    @property
    def population(self):
        """
        :return: the state population
        """
        return self._population

    @population.setter
    def population(self, value):
        """
        sets the state population to the specified value
        :param value the new population of the state
        """
        self._population = value

    @property
    def region(self):
        """
        :return: the state region
        """
        return self._region

    @region.setter
    def region(self, value):
        """
        sets the state region to the specified value
        :param value the new region of the state
        """
        self._region = value

    @property
    def seats(self):
        """
        :return: the state US House Seats
        """
        return self._seats

    @seats.setter
    def seats(self, value):
        """
        sets the state US House Seats to the specified value
        :param value the new US House Seats of the state
        """
        self._seats = value

    def formatted_str(self):
        """
        :return: a formatted string containing all info about the state
        """
        return "%-17s: %s\n%-17s: %s\n%-17s: %s\n%-17s: %s\n%-17s: %s\n%-17s: %s\n" % (
            "State Name", self.name,
            "Capital City", self.capital,
            "State Abbr", self.abbr,
            "State Population", "{:,}".format(self.population),
            "Region", self.region,
            "US House Seats", self.seats
        )

    def __gt__(self, other):
        return self.name() > other.name()

    def __str__(self):
        return "[%s, %s, %s, %s, %s, %s]" % (
            self._name, self._capital, self._abbr,
            self._population, self._region, self._seats
        )
