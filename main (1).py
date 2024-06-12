print("Hello World")

#create a variable to store my name 
name = "Lav" 

#print my name is Lav 
print("My name is", name, sep="---")

#create a variable to store my last name 
last_name= "Patel"

#write a statement to display "My full name is firstname lastname)
print( "My full name is", name, last_name, sep="---")

#create a variable to store the sport I play 
sport = "tennis"

#print the sport I play is tennis 
print("I love to play",sport)

#create a variable to store my age and weight
age = 16
weight = 175.7
half_age = age / 2

#print a sentence with my name, age and weight 
print(f"My name is {name} {last_name}. \nI am {age} years old and I weigh {weight}lbs")


#get and print the data type for age and weigth and half_age
print(type(age))
print(type(weight))
print(type(half_age))

#write 3 print statements using string interpolation (f string) to print descriptive sentences for the datatypes
# variable age is an int
# variable weight is a float
# variable half age is a float 

print(f"Variable age is a {type(age)}")
print(f"varibale weight is a {type(weight)}")
print(f"Variable half_age is a {type(half_age)}")

number_1= "5"
number_2= "7"
total = number_1 + number_2
print(f"Total:{total}")