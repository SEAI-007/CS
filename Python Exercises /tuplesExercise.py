# 1. Create a Tuple
my_tuple = ("Mercedes","BMW","VW","Audi","Porsche")

# 2. Print the Tuple
print(my_tuple)

# 3. Access Tuple Items
print(my_tuple[0])
print(my_tuple[-1])

# 4. Slice the Tuple
print(my_tuple[1:3])
print(my_tuple[0:2])
print(my_tuple[2:6])


# 5. Check if an Item Exists
if "Rolls Royce" in my_tuple:
    print("Rolls Royce in your tuple")
else:
    print("You are broke")


# 6. Count and Index
print(my_tuple.count("VW"))

# 7. Packing and Unpacking
beginning, *mid, end = my_tuple
print(beginning, mid, end)

# 8. Joining Tuples
another_tuple = ("this", "is", "another", "tuple")
print(my_tuple + another_tuple)
print(my_tuple*2)   #also works with lists