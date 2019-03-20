"""
Stephen Shappley
N01184718
CAP4630 - Spring 2019
"""

from subprocess import Popen, PIPE


def main():
    process = Popen(["clasp", "0", "cnf_test.txt"], stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    print(out)


main()
