#Exercise One
products = [
    ("Laptop", 1200, True),
    ("Mouse", 25, False),
    ("Keyboard", 80, True),
    ("Webcam", 40, True),
    ("Monitor", 700, False),
]

#Task one
discounted_products = []
for product in products:
    if product[1] > 50 and product[2]== True:
        discounted_products.append((product[0],product[1]*0.8))
                                
print(discounted_products)

#Task two
for product in products:
    if product[2] == False:
        print(f"Following Item must be restocked: {product[0]}")

#Task Three
total_inventory = 0
for product in products:
    if product[2] == True:
        total_inventory += product[1]
print("Total inventory value: " + str(total_inventory))

#Exercise Two
users = [
    {"id": 1, "name": "Alice", "role": "Admin", "status": "Active"},
    {"id": 2, "name": "Bob", "role": "User", "status": "Away"},
    {"id": 3, "name": "Charlie", "role": "User", "status": "Active"},
    {"id": 4, "name": "Diana", "role": "Moderator", "status": "Busy"},
    {"id": 5, "name": "Ethan", "role": "User", "status": "Active"}
]



#Task one
iterator = 0
index = -1
for user in users:
    print(users[iterator - 1]["name"].upper())
    iterator -= 1
    index += 1
    if index == 2:
        break

# GPT Solution:
# for user in reversed(users[:3]):
#     print(user["name"].upper())


#Task two

iterator = 0
for user in users:
    print(users[iterator - 1]["name"].upper())
    users[iterator - 1].update({"email":users[iterator - 1]["name"].lower()+"@gmail.com"})
    print(users[iterator - 1])
    iterator -= 1


#Task three
iterator = 0
for user in users:
    if user["status"] == "Active":
        iterator += 1
print(iterator)


