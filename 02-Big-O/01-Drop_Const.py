# this runs 2 loops with O(n) each so O(n + n )times that is O(2n) 
#  where the numericals 1 to n number of loops  are constant
#  so drop the constants and its is just O(n)
def print_items(n):
    #this is O(n)
    for i in range(n):
        print(i)
    #this is O(n)
    for j in range(n):
        print(j)

print_items(10)


