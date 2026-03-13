# Step 1 Create variables
name ="Efecan Güler"
age = 25
height =1.87

# Step 2 Print the variables
print(name,age,height)

# Step 3: Check the type of the variables
age_str = str(age)

# Step 4: Casting
print(type(name), type(age), type(height))
print(f"My Name is Alice and I am {age_str} years old")

# Bonus: Global Variable (Bonus)
global_message = "GLOBALMESSAGE"
def global_variable_function():
    globalo: str = input("Input your manipulation message: ")
    print("The word manipulated is " + global_message + globalo)

global_variable_function()