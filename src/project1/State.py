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
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def capital(self):
        return self._capital

    @capital.setter
    def capital(self, value):
        self._capital = value

    @property
    def abbr(self):
        return self._abbr

    @abbr.setter
    def abbr(self, value):
        self._abbr = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value

    def formatted_str(self):
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
