"""
Stephen Shappley
N01184718@ospreys.unf.edu
"""

import csv
from States import States
from State import State


def read_states_csv(filename):
    """
    Reads in the specified CSV file. Returns a list containing the content as State objects.
    :param filename: The name of the file you want to read
    """
    data = []
    with open(filename) as handler:
        reader = csv.reader(handler)
        n = 0
        for row in reader:
            if n != 0:
                state = State(row[0], row[1], row[2], int(row[3]), row[4], row[5])
                data.append(state)
            n = n + 1
    return data


def prompt_user():
    """
    Prompts the user to select an option.
    Loops until the user enters something valid.
    :return: the valid number the user entered
    """
    i = 0
    invalid = True
    while invalid:
        i = raw_input("1) Print State Report\n"
                      "2) Sort by State Name\n"
                      "3) Sort by Population\n"
                      "4) Search by State Name\n"
                      "5) Quit\n"
                      ": ")
        if i.isdigit():
            i = int(i)
            invalid = i < 1 or i > 5
        else:
            invalid = True
        if invalid:
            print "Invalid selection '%s'" % i
    return i


def main():
    data = read_states_csv("States.csv")
    states = States(data)
    selection = 0
    while selection != 5:
        selection = prompt_user()
        if selection == 1:
            states.report()
        elif selection == 2:
            states.sort_by_name()
            print "Sorted States by Name"
        elif selection == 3:
            states.sort_by_population()
            print "Sorted States by Population"
        elif selection == 4:
            name = raw_input("Enter state name: ")
            result = states.search_by_name(name)
            if result is None:
                print "No such state found: '%s'" % name
            else:
                print result.formatted_str()
        print ""


main()
