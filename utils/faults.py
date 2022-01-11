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

import numpy as np

class Faults:
    def __init__(self,algorithm, num_pages):
        self.algorithm = algorithm
        self.num_pages = num_pages
        self.pages = self.gen_pages(num_pages)
        self.faults = self.getFaults()

    def gen_pages(self, num_pages):
        pages = np.random.randint(11, size=num_pages)
        return pages
    
    def getFaults(self):
        if self.algorithm == "OPT":
            return OPT.page_faults(self, self.num_pages)
        elif self.algorithm == "LRU":
            return LRU.page_faults(self, self.num_pages)
        elif self.algorithm == "FIFO":
            return FIFO.page_faults(self, self.num_pages)
        else:
            return "Invalid algorithm"

class FIFO(Faults):
    def __init__(self, num_pages):
        Faults.__init__(self, "FIFO", num_pages)
        self.num_pages = num_pages
        self.faults = FIFO.page_faults(self, num_pages)

    def page_faults(self, num_pages):
        self.num_pages = num_pages
        pages = self.pages
        mem = []  #list of frames
        queue = [] #queue to track page reference order
        page_faults = 0 #number of page faults
        i=0 #index of pages

        for page in pages:
            if i<num_pages: #if frames not full
                if page not in mem: #if page not in memory
                    mem.append(page)
                    queue.append(page)
                    i+=1
                    page_faults+=1

            else:
                if page not in mem:
                    q = queue.pop(0) #pop the first element of the queue (FIFO)
                    queue.append(page) #add new page to queue
                    j = mem.index(q) #get the index page to evict
                    mem[j] = page #replace page
                    page_faults+=1

        #return number of page faults
        return page_faults 

class LRU(Faults):
    def __init__(self, num_pages):
        Faults.__init__(self, "LRU", num_pages)
        self.num_pages = num_pages
        self.faults = LRU.page_faults(self, num_pages)
    
    def page_faults(self, num_pages):
        self.num_pages = num_pages
        pages = self.pages
        mem = []
        usage = [] #list to track page reference order
        page_faults = 0
        i=0

        for page in pages:
            if i < num_pages:
                if page in usage: #if page has been used, add it to front of list
                    usage.remove(page)
                
                usage.insert(0,page)
                if page not in mem: #if page not in memory, add it
                    mem.append(page)
                    i+=1
                    page_faults+=1

            else:
                if page in usage: #if page has been used, add it to front of list
                    usage.remove(page)
                usage.insert(0,page)
                if page not in mem: #if page not in memory
                    q = usage.pop(-1) #remove last element of the list (least used page)
                    j = mem.index(q) #get the index page to evict
                    mem[j] = page
                    page_faults+=1

        # return number of page faults
        return page_faults

class OPT(Faults):
    def __init__(self, num_pages):
        Faults.__init__(self, "OPT", num_pages)
        self.num_pages = num_pages
        self.faults = OPT.page_faults(self, num_pages)
    
    def page_faults(self, num_pages):
        self.num_pages = num_pages
        pages = self.pages
        mem = []
        i = 0 #frame use counter
        n = 0 #page reference index counter
        page_faults = 0


        for page in pages:
            if i<num_pages:
                if page not in mem:
                    mem.append(page)
                    i+=1
                    page_faults+=1
                n+=1

            else:
                if page not in mem:
                    #create a usage list, with the index of the page in the future references, else 100000000
                    usage = [pages[n::].index(m) if m in pages[n:] else 100000000 for m in mem]
                    u = usage.index(max(usage)) #get the index of the maximum element in the usage list (page not reference in future or furthest ref)
                    mem[u] = page
                    page_faults+=1
                n+=1

        return page_faults
