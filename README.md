# Greedy-Set-Cover

An algorithm that approximately calculates the set cover, given a list of subsets and a target set.

The algorithm accepts an adjacency matrix as an input. This is to be passed in a text file. The first row of the text file should represent the target set. 
Let n be the length of a row. Each row represents a subset S of the numbers 1, ..., n. A 1 in the ith position of a row indicates i∈S and a 0 indicates i∉S. 

For example, the subset S={1,4,5,7} is to be provided as 1001101. 

The code also computes the optimal subset selection if needed.
The output is a list of the selected subsets in the adjacency matric form.
