#  1. Create a Set
fruits = {"apple", "banana", "cherry", "dragonfruit", "orange"}
print(fruits)


# 2. Check Membership
if "apple" in fruits: print("Apple is in fruits")

# 3. Add and Update Items
fruits.add("mango")
print(fruits)
more_fruits = {"strawberry", "blackberry", "raspberry"}
fruits.update(more_fruits)
print(fruits)


# 4. Remove Items
fruits.remove("mango")
print(fruits)

# 5. Set Operations 
set_a = {"apple, banana, pineapple","grape"}
set_b = {"watermelon", "grape"}
print(set_a.union(set_b))
print("------------")
print(f"Intersektion ist: {set_a.intersection(set_b)}")
print(f"Difference ist:  {set_a.difference(set_b)}")
print(f"Symmetric difference ist: {set_a.symmetric_difference(set_b)}")

# 6. In-place Set Operations
print("------------")
print(f"set a: {set_a}")
print(f"set b: {set_b}")
set_a.difference_update(set_b)
print(f"Nach dem Different Update: {set_a}")
set_a.intersection_update(set_a)
print(f"Nach dem Intersection Update: {set_a}")
set_a.update(set_b)
print(f"Nach dem Update: {set_a}")

# 7. Relational Methods
small_set = {"a", "small","set"}
large_set = {"large", "set", "random", "word", "like","a", "small"}
print(small_set.issubset(large_set)) #checks if ALL the values in small_set are a part of large_set
print(large_set.issuperset(small_set))
print(small_set.isdisjoint(large_set)) #checks if they have NOTHING in common.