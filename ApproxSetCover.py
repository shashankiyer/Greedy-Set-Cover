'''
Computes an approximate minimal set cover using a polynomial-time-r(n)-approximation algorithm

:author Shashank
'''
from __future__ import print_function
import argparse
import os
from itertools import permutations

NO_OF_NODES = 0

def determine_min_cost(U, F):
    '''
    Finds the set that maximises S ∪ U for S ∈ F

    :param U : The elements that are still left to be covered
    :param F : The list of subsets

    :return Si : The subset that will minimise U the most
    '''
    cost = 0
    Si = set()
    for S in F:
        temp_max = len(set(S).intersection(U))
        if cost < temp_max:
            cost = temp_max
            Si = S
    return Si


def greedy_set_cover(X, F):
    '''
    Computes a minimal set cover

    :param X: The target set
    :param F: The list of subsets

    :return C: The minimal set cover
    '''
    U = set(X)
    C=[]
    C_set = set(C)

    while len(U) > 0:
        S = determine_min_cost(U, F)
        C.append(S)
        C_set = C_set.union(S)
        U = U.difference(C_set)

    return C

def brute_force_set_cover(X, F):
    '''
    Computes the minimal set cover by iterating over all permutations of
    the set cover

    :param X: The target set
    :param F: The list of subsets

    :return C: The minimal set cover
    '''
    C_min = F
    for ff in list(permutations(F)):
        C=[]
        U = set(X)
        C_set = set(C)
        iterator = 0

        while len(U) > 0:
            f = ff[iterator]
            if C_set.union(f) != C_set:
                C.append(f)
                C_set = C_set.union(f)
                U = U.difference(C_set)
            iterator+= 1
        if len(C_min) > len(C):
            C_min = C

    return C_min    

def create_adjacency_matrix(C):
    '''
    A function that outputs the list of selected subsets in their 
    adjacency matrix form.

    :param C: The list of selected subsets
    :return: An adjacency matrix
    '''
    adj_matrix = []
    for c in C:
        curr_set = set(c)
        adj=[]
        for i in range (1, NO_OF_NODES+1):
            if i in curr_set:
                adj.append(1)
            else:
                adj.append(0)
        adj_matrix.append(adj)

    return adj_matrix
    
def parse_adjacency_matrix_file(filename):
    '''
    A function for parsing the adjacency matrix from text data in .txt file.

    :param filename: The path of the matrix file
    :return: The parsed vectors X and F
    '''

    if not os.path.exists(filename):
        raise Exception('Graph file not found')

    F=[]
    global NO_OF_NODES

    with open(filename, 'r') as f:
        for line in (f):
            ff = []
            count = 1
            for j in line:
                if j == "1":
                    ff.append(count)
                count = count + 1
            
            F.append(ff)
            NO_OF_NODES = len(line)
            
    X = F[0]
    F.pop(0)
    return X, F


parser = argparse.ArgumentParser(
    description='Computes the Maximal Subset',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='For further questions see the README'
)

parser.add_argument(
    'some_file_with_list_of_sets',
    help='Path to the file containing comma-separated vector data'
)


if __name__ == '__main__':
    args = parser.parse_args()

    X, F = parse_adjacency_matrix_file(args.some_file_with_list_of_sets)

    p = create_adjacency_matrix(greedy_set_cover(X, F))
    for i in p:
        print(*i,sep='')

    print()

    p = create_adjacency_matrix(brute_force_set_cover(X, F))
    for i in p:
        print(*i,sep='')
