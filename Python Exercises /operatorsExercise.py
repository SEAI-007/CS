#Exercise 1: Arithmetic Operators
a = 15
b = 4
print(a-b, a+b, a*b, a/b, a%b, a//b, a**b)

#Exercise 2: Assignment Operators
x = 10
print(x)
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x/= 2
print(x,type(x))

#Exercise 3:Comparison Operators 
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

#Exercise 4: Logical Operators
print("Exercise 4")
is_python_fun = True
is_java_fun = False
print(is_python_fun and is_java_fun)
print(is_python_fun or is_java_fun)
print(not is_python_fun)

#Exercise 5: Identitiy Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("Exercise 5")
print(list1 is list3) #Returns false, because the OBJECT is not the same, but the values are
print(list1 is list2) #Returns true, because it is the same Object

#Exercise 6: Membership Operators
text = "Python programming is fun!"
print ("Python" in text) #returns true
print("Java" not in text) #returns true

#Exercise 7 Bitwise Operators (Bonus)
a=5
b=3
print("Exercise 6")
print (f"Bitwise AND &: {a & b}")
print (f"Bitwise OR |: {a | b}")
print (f"Bitwise XOR ^: {a ^ b}")
print (f"Bitwise XOR ^: {a ^ b}")

#Exercise 8 Operator Precedence
print("Exercise 8")
print(2**2**3) #this is being read from right to left
print((2**2)**3)