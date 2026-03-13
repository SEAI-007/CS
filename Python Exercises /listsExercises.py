# Step 1: Create and Print a List
fruits = ["apple", "banana", "passionfruit", "kiwi", "orange"]
print(fruits)

# Step 2: Access Elements by Index and Negative Index
print(fruits[0],fruits[-1])

# Step: 3 Slice a List
print("Step 3")
print(fruits[0:2])
print(fruits[2:5])
# Step 4: Check if an Item Exists
print("Step 4")
if "apple" in fruits: 
    print("Apple was found in fruits")

# Step 5: Add Items
print("Step 5")
fruits.append("dragonfruit") #just appends it to last position
fruits.insert(1,"grape") #inserts it at a specific location
print(fruits)

# Step 6: Change Items
print("Step 6")
fruits[3] = "mango"
print(fruits)

# Step 7: Remove items
print("Step 7")
fruits.remove("dragonfruit")
print(fruits)
fruits.pop(1)
print(fruits)
#fruits.clear()
print(fruits)

# Step 8: Copy a list
print("Step 8")
fruits_copy = fruits.copy()
fruits_copy_2 = fruits
fruits.pop(1)
print(fruits)
print(fruits_copy)
print(fruits_copy_2)

# Step 9: Concatenate and Extend
print("Step 9")
cars = ["Mercedes", "BMW", "VW"]
names = ["Heinrich", "Lisa", "Detlef"]
print(cars + names)
names.extend(cars)
print(names)

# Step 10: Sort and Reverse
print("- Step 10 -")
names.sort()
print(names)
names.reverse()
print(names)
names_sorted = sorted(names) #Doesn't change the origin and returns new list
print(names, names_sorted)

# Count and Index
print("- Step 11 -")
print(names_sorted.count("Mercedes"))
print(names_sorted.index("Lisa"))

# List comprehension
print("- Step 12 -")
print([x.upper() for x in names_sorted if len(x)>5]) # Do this / for every / when