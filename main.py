# Define a class named Faults and its subclass of page replacement policy in paging system (Optimal, LRU, FIFO).
# The Faults class has
#   - an init function which takes the replacement algorithm as (OPT, LRU, FIF)
#   - number of page references from user
#       - generate random integers from 0 to 10
#       - store them in a list

# init should 
#   -take number of pages in physical memory.
# 
# Finally that class method should return the number of page fault for that algorithm.

from utils.faults import *

def main():
    num_pages = int(input("Enter number of pages: "))
    algorithm = ''
    while algorithm not in ('OPT', 'LRU', 'FIFO'):
        algorithm = input("Enter algorithm (OPT/LRU/FIFO): ")

    faults = Faults(algorithm, num_pages)

    print("Randomly Generated Page References: ", faults.pages)

    print("Number of page faults: ", faults.faults)

if __name__ == "__main__":
    main()