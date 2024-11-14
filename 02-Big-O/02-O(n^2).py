# n times n items O(n * n) are printing which is O(n^2) 
# the  nested for loop, less efficient from time complexity stand point
def print_items(n):
    #this is O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j) 

print_items(10)

