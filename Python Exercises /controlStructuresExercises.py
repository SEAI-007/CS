# 1. Basic If Condition
number = 5
if number > 0:
    print("the number is negative")
elif number == 0:
    print("The number is exactly 0")
else:
    print("The number is negative")

# 2. Grade Calculator

score = 78
if score >= 90:
    print("A")
elif  90 > score >= 80:
    print("B")
elif  80 > score >= 60:
    print("C")
else:
    print("D")


# 3. Ternary Operator Practice
age = 18
status=""
status = "adult" if age >= 18 else "minor"
print(status)

# 4. For Loop over a List
car_brands = [
    "Toyota",
    "Honda",
    "Ford",
    "Chevrolet",
    "BMW",
    "Mercedes-Benz"
]

for car in car_brands:
    print(f"{car} is in the list")

# 5. For Loop with Conditions
for i in range(1,10):
    if i%2 == 0:
        print(i)


# 6. While Loop Summation
index = 1
tota_value = 0
while index <= 100:
    tota_value += index
    index += 1
print(tota_value)


# 7. Break out of a Loop
for car in car_brands:
    if len(car) > 5:
        print(car)
        break

# 8. Nested Loops
people = ["Alice", "Bob", "Charlie", "Dustin"]
pets = ["dog","cat", "monkey", "rat"]
for people in people:
    for pet in pets:
        print(people + " " + pet) 


# 9. Loop with Else Clause
people = ["Alice", "Bob", "Charlie", "Dustin"]
for i in people:
    print(i)
    if i == "Charlie":
        print("Success")
        break
else: print("no Success")


# 10. Pass Statement Usage
for i in people:
    pass


# 11. Pattern matching
fruits = ["apple", "banana", "orange"]
veggies = ["carrot", "broccoli", "spinach"]
meat = ["chicken", "beef", "pork"]
item = "apple"

if item in fruits:
    match fruits:
        case ["apple", "banana", "orange"]:
            print("It's a fruit")
    
elif item in veggies:
    match veggies:
        case ["carrot", "broccoli", "spinach"]:
            print("It's a veggie")
else:
    match meat:
        case ["chicken", "beef", "pork"]:
            print("It's meat")
    