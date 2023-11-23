#!/usr/bin/env python3
from polka.tools import calculate_routeid, print_poly
DEBUG = False

def _main():
    print("Insering irred poly (node-ID)...")
    s = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],  # s1 - CRC ignora o primeiro 1
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],  # s2
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],  # s3
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],  # s4
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],  # s5
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],  # s6
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],  # s7
    ]

    #===========================================================#
    print("\nFrom h1 to the others ===========================")
    # defining the nodes from h1 to h4
    nodes = [
        s[0],
        s[1],
        s[2],
        s[3],
        s[4],
        s[5],
        s[6]
    ]
    # defining the transmission state for each node from h1 to h4
    o = [
        [1, 1, 0], # s1
        [0, 1, 0], # s2
        [0, 1, 0], # s3
        [0, 1, 0], # s4
        [0, 1, 0], # s5
        [1, 1, 0], # s6
        [0, 1, 0]  # s7
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    #===========================================================#
    print("\nFrom h2 to h1 ===================================")
    # defining the nodes from h2 to h1
    nodes = [
        s[2],
        s[4],
        s[0]
    ]
    # defining the transmission state for each node from h2 to h1
    o = [
        [0, 0, 1], # s3
        [0, 0, 1], # s5
        [0, 0, 1] # s1
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    #===========================================================#
    print('\n From h3 to h1==================================')
    nodes = [
        s[3],   #s4
        s[5],   #s6
        s[1],   #s2
        s[0]    #s1
    ]

    o = [
        [0,0,1],   #s4 
        [0,0,1],   #s6 
        [0,0,1],   #s2 
        [0,0,1]    #s1           
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    #===========================================================#
    print('\nFrom h4 to h1==================================')
    nodes = [
        s[6],   #s7
        s[5],   #s6
        s[1],   #s2
        s[0]    #s1
    ]

    o = [
        [0,0,1],   #s7 
        [0,0,1],   #s6 
        [0,0,1],   #s2 
        [0,0,1]    #s1 
    ]

    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    #===========================================================#
    print('\nFrom h2 to the others===========================')
    nodes = [
        s[0],
        s[1],
        s[2],
        s[3],
        s[4],
        s[5],
        s[6]
    ]

    o = [
        [1, 0, 1], # s1
        [0, 1, 0], # s2
        [0, 0, 1], # s3
        [0, 1, 0], # s4
        [0, 0, 1], # s5
        [1, 1, 0], # s6
        [0, 1, 0]  # s7
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    #===========================================================#
    print('\nFrom h3 to the others===========================')
    nodes = [
        s[0],
        s[1],
        s[2],
        s[3],
        s[4],
        s[5],
        s[6]
    ]

    o = [
        [0, 1, 1], # s1
        [0, 0, 1], # s2
        [0, 1, 0], # s3
        [0, 0, 1], # s4
        [0, 1, 0], # s5
        [1, 0, 1], # s6
        [0, 1, 0]  # s7
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    #===========================================================#
    print('\nFrom h4 to the others===========================')
    nodes = [
        s[0],
        s[1],
        s[2],
        s[3],
        s[4],
        s[5],
        s[6]
    ]

    o = [
        [0, 1, 1], # s1
        [0, 0, 1], # s2
        [0, 1, 0], # s3
        [0, 1, 0], # s4
        [0, 1, 0], # s5
        [0, 1, 1], # s6
        [0, 0, 1]  # s7
    ]
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

if __name__ == '__main__':
    _main()
