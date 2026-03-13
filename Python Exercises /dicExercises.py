# 1. Create and Print a Dictionary
person = {
    "name": "Efe", 
    "age": 25,
    "city": "Leverkusen"
    }
print(person)


# 2. Access Dictionary Elements
print(person["name"])
print(person.get("email"))
print(f"Die Keys sind: {person.keys()}")
print(f"Die Values sind: {person.values()}")
print(f"Die Items sind: {person.items()}")


# 3. Check for Key Existence
print("age" in person)


# 4. Change and Update Dictionary Elements
person["city"] = "Zürich"
person.update({"occupation": "Fullstack engineer"})
print(person)

# 5. Add New Items to the Dictionary
person["country"] = "Switzerland"
person.update({"hobby":"gaming"})
print(person)


# 6. Remove Items from the Dictionary
person.pop("hobby")
print(person)
removed_item = person.popitem()
print(removed_item)
print(person)
del(person["city"])
print(person)
# person.clear()
# print(person)

# 7. Copy a Dictionary
person_copy = person.copy()
person.pop("age")
print(person_copy,person)

# 8. Using setdefault()
print(person.setdefault("name"))
print(person.setdefault("Race"))