# totally O(n^2 + n) if n=100 so n^2 is 10,000 where n is  small (100)
# where as n^2 is big & dominant(10,000) 
# so drop the non dominants, smaal and standalone n. so its just O(n^2)
def print_items(n):
    #this is O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j)
    #this is O(n)
    for k in range(n):
        print(k)

print_items(10)

