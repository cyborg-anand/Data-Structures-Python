#Though it looklike 2 O(n) but it is not O(n) actually it is O(a+b) 
#If two for loops were nested then it is O(a*b)
def print_items(a,b):
    #this is O(a)
    for i in range(a):
        print(i)
        #this is O(b)
    for j in range(b):
        print(j)

print_items(1, 10)
