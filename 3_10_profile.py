# Create:
# person - a list that stores the following items:

# tuple that stores "first name and "John".

# tuple that stores "last name" and "Doe".
# tuple that stores "birthdate" and "12-12-1986".

# tuple that stores the string "age" and an integer number with the age of the person.
# tuple that stores the "favorite color" and "blue".

person = [('first_name', 'John'), ('last_name', 'Doe'), ('birthdate', '12-12-1989'), ('age', 39), ('favorite_color', 'blue')]
# people - an empty list. 
people = []
# favorite_foods - a tuple that stores:
favorite_foods = ('favorite foods', ['hamburger', 'pasta', 'pizza'])
# hobbies - a list that stores:
hobbies = ['hobbies', 'traveling', 'reading']
#movies - a list that stores:
movies = ['favorite movies', 'star wars', 'Avengers']
print(type(person))
print(person)

# profile - a dictionary with a key for each letter in the string alphabet. 
# Each key should have an empty dictionary as its value.
import string

alphabet = string.ascii_lowercase
alphabet_dict = {char: {} for char in alphabet}

print(alphabet_dict)

# Update the list inside the favorite_foods tuple: 
favorite_foods = list(favorite_foods)
favorite_foods.append('icecream')
favorite_foods.append('jelly')
favorite_foods.pop(0)
favorite_foods = tuple(favorite_foods)
print(favorite_foods)

# Update the list inside the hobbies tuple: 
hobbies =list(hobbies)
hobbies.append('cooking')
hobbies.insert(2, 'music')
hobbies[0] = hobbies[2]
hobbies.pop()
hobbies = tuple(hobbies)
print(hobbies)

# Update list insi the movies
movies.pop(0)
movies.append('new')
movies.append('latest')
movies[-1] = 'et'
print(movies)

# Remove duplicates from our lists:
favorite_foods = set(favorite_foods)
hobbies = set(hobbies)
favorite_foods = tuple(favorite_foods)
hobbies = tuple(hobbies)

# Store all the data in the person list:
person.insert(3, hobbies)
print(person)