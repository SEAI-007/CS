from pprint import pprint
from datetime import date
# Step 1
person = ("Alice", 34);
favorite_foods = ["Pizza"];
hobbies = ["Reading"];
profile = {};

# Step 2
# favorite_foods.append("Sushi");
# favorite_foods.append("Pasta");
# favorite_foods.append("Hamburger");

favorite_foods.extend(["Sushi", "Pasta", "Hamburger"]);
print(favorite_foods)

favorite_foods.remove("Sushi");
print(favorite_foods)

favorite_foods[-1] = "Pizza"
print(favorite_foods)

# Step 3 

hobbies.extend(["Writing", "Traveling", "Reading"]);
print(hobbies)

hobbies.pop(-1)
print(hobbies)

hobbies[0] = hobbies[-1]
print(hobbies)

hobbies.append("Reading");

# Step 4
hobbies = list(set(hobbies))
print(hobbies)

favorite_foods = list(set(favorite_foods))
print(favorite_foods)

# Step 5 
profile["name"] = person[0];
profile["age"] = person[1];
profile["hobbies"] = hobbies;
profile["favorite_foods"] = favorite_foods;

# Step 6
print(profile["name"])
print(profile["age"])
print(profile["hobbies"])
print(profile["favorite_foods"])
print(profile.keys())
for key in profile.keys():
    print(key)
print(profile.values())
for value in profile.values():
    print(value)

for key, value in profile.items():
    print(key, value)
pprint(profile, indent=4)

# Step 7 
profile["name"] = "Maria";
current_year = date.today().year;
profile["age"] = current_year - 1990;
print(profile["name"]);
print(profile["age"]);

# Step 8 
profile["movies"] = ["The Matrix", "Star Wars", "Interstellar"];
profile["hobbies"].append("Running");
print(profile["movies"]);
print(profile["hobbies"]);

# Step 9
profile["favorite_foods"][-1] = "Hamburger";
profile["favorite_foods"].sort();
print(profile["favorite_foods"]);

# Step 10
pprint(profile, indent=4)

