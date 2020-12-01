# Python code to demonstrate working of 
# heappushpop() and heapreplace()

# importing "heapq" to implement heap queue
import heapq

# initializing list 1 
li1 = [5, 7, 9, 4, 3]

# initializing list 2 
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert ist into heap 
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously 
# pops 2 
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li1, 2))

# using heappushpop() to push and pop items simultaneously 
# pops 3 
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li2, 2))
