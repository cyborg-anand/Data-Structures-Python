#So the previous big O's that we've seen was as n gets bigger the number of operations increases.
#But in this case the only operation is the addition
#So if n is one you have one operation.
#If n is million, you still have one operation and that is O of one.
#whatever the N is the operation is one (addition) si it is O(1)
# As n increases we are not increasing the number of operations
#Most efficient Big O
def add_items(n):
    return n + n + n
 
sum=add_items(10)
print (sum)