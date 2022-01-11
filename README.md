# Page Replacement Algorithm

In this minor project, we will implement page replacement algorithms i.e. Optimal, LRU, FIFO. We take input from the user as the number of pages, and the Algorithm. The pages are randomly generated using numPy and print the results as the number of faults.

**Given Problem Statement:**

*Define a class named Faults and its subclass of page replacement policy in paging system (Optimal, LRU, FIFO). The Faults class has an init function which takes the replacement algorithm as (OPT, LRU, FIF) and number of page references from user and generate random integers from 0 to 10, init should also take number of pages in physical memory. Finally that class  method should return the number of page fault for that algorithm.*

## Steps to RUN the program

- Git clone the repository
- Go to the directory and run the following command:


    - Install numPy
        ```bash
        pip install numpy
        ```
    - Run the code
        ```
        python3 main.py
        ```
- You will be prompted to enter the number of pages, Algorithm.


- Output will be the number of page faults.
