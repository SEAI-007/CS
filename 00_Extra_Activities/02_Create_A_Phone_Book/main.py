from pprint import pprint
# Step 1
alphabelt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
phone_book = {};

# Step 2
for letter in alphabelt:
    phone_book[letter] = {};

# Step 3
pprint(phone_book);
print(phone_book.keys());

# Step 4
phone_book["A"]["Alice"] = "123-456-7890"
phone_book["A"]["Ally"] = "132-456-7908"
phone_book["A"]["Ammy"] = "113-556-7908"

# Step 5
print(phone_book["A"].keys());
for name in phone_book["A"].keys():
    print(name)

print(phone_book["A"].values());

for phone in phone_book["A"].values():
    print(phone)

print(phone_book["A"])

# Step 6
phone_book["C"]["Cally"] = "333-456-7890"
phone_book["C"]["Casper"] = "222-456-7908"
phone_book["C"]["Clint"] = "122-556-7908"
print(phone_book["C"].keys());
print(phone_book["C"].values());

phone_book["M"]["Mike"] = "123-444-7890"
phone_book["M"]["Mary"] = "132-666-7908"
phone_book["M"]["Monica"] = "113-555-7908"
print(phone_book["M"].keys());
print(phone_book["M"].values());

phone_book["P"]["Paul"] = "123-456-7790"
phone_book["P"]["Paulette"] = "132-456-8808"
phone_book["P"]["Pete"] = "113-556-5508"
print(phone_book["P"].keys());
print(phone_book["P"].values());

# Step 7
print(phone_book.keys());
for letter in phone_book:
    print(letter)


# Step 8
print(phone_book.values());

for value in phone_book.values():
    print(value);

for key, value in phone_book.items():
    print(f"{key}: {value}")

# BONUS
name = "mike";
phone = "111-111-8808";

for person in phone_book[name[0].upper()].keys():
    if name.capitalize() == person:
        print(f"{person} is in the phonebook");

for letter in phone_book:
    for person, phone_number in phone_book[letter].items():
        if phone == phone_number:
            print(f"{phone} is in the phonebook under the name {person}");
        else:            
            print(f"{phone} is not in the phonebook");