# num1 = 11

# num2 = num1

# print("Before num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2)) 

# num2 = 22 

# print("\nAfter num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2) 

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

# num1 = 33 

# print("\nAfter num1 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2) 

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

# num1 = 11 

# print("\nAfter num1 value is updated to 11 again:")
# print("num1 =", num1)
# print("num2 =", num2) 

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))


#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("-------------------------------------")
dict3={
         'value': 33
        } 
dict2 = dict3 
print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 
print("dict3 =", dict3)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("dict3 points to:", id(dict3))
print("-------------------------------------")
dict1 = dict2 
print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 
print("dict3 =", dict3)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("dict3 points to:", id(dict3))
# dict2={
#          'value': 22
#         } 