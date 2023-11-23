#!/usr/bin/env python3
from polka.tools import calculate_routeid, print_poly
DEBUG = False


def _main():
    print("Insering irred poly (node-ID)")
    s = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],  # s4
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],  # s6
    ]
    print("From h1 to h2 ====")
    # defining the nodes from h1 to h2
    nodes = [
        s[0],
        s[1],
    ]
    # defining the transmission state for each node from h1 to h2
    o = [
        [1, 0, 0, 0], # s4
        [0, 0, 0, 1], # s6
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    #Definindo routeID de volta
    print("From h2 to h1 ====")
    # defining the nodes from h2 to h1
    nodes = [
        s[0],
        s[1],
    ]
    # defining the transmission state for each node from h2 to h1
    o = [
        [0, 0, 0, 1], # s4
        [0, 0, 1, 0], # s6
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))


if __name__ == '__main__':
    _main()
