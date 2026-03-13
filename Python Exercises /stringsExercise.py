#Step 1: Create Strings
first_name = "Efecan"
last_name = "Güler"
age = 25
bio = """This is my Bio:
Lorem ipsum dolor etc.
I'm learning Python, not C# right now."""

#Step 2 Access Characters and Slice Strings
print(first_name[0],last_name[1])

#Step 3: Loop through a String:
for x in first_name:
    print(x)

#Step 4: String Length
print(len(bio))

#Step 5: Check Substrings
python_find = bio.find("Python")
java_find = bio.find("Java")

if python_find == -1:
    print(f"The value is {python_find} therefore there is no python in bio")
else:
    print(f"The value is {python_find} therefore there is python in bio")
if java_find == -1:
    print(f"The value is {java_find} therefore there is no java in bio")
else:
    print(f"The value is {java_find} therefore there is java in bio")

#Step 6: Modify Strings:
first_name.upper()
last_name.lower()

bio_no_space = bio.strip().replace("python", "coding").split() #Chaining!!!
print(bio_no_space)

#Step 7: Concatenate Strings
full_name = first_name + " " + last_name
print(full_name)

#Step 8: Strong Formatting
print(f"Hello my name is {full_name} and I love python")
print("My full name is {}, and I am {} years old.".format(full_name,age))

#Step 9: Escape Characters
print("He said, Python's great!'")
print('He said "Python\'s great!"')

#Step 10: Bonus: Use string methods to display
#print(bio.center(50)) -> doesn't work because the String is multi lined
print(full_name.count("a"))