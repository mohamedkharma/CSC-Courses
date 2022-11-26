#	Name: Mohamed Kharma
#	Lab Assignment 1

#	Question 1
print("""Program to convert minutes to milliseconds
for example if the user input 3 as the number
of minutes, then the output 180000 milliseconds.
	""")
number_of_minutes = int(input("Enter the number of minutes you would like to convert: "))
milliseconds = number_of_minutes * 60000

print("In", number_of_minutes, "minutes, there is :", milliseconds, "milliseconds")

#	Question 2
from math import sqrt
a,b,c = 1,2,1
discriminant = (b**2) - (4 * a * c)
quad1 = (-b - sqrt(discriminant)) / (2 * a)
quad2 = (-b + sqrt(discriminant)) / (2 * a)

print("X1=", quad1, "\nX2=", quad2)

#	Question 3
print("""Program to calculate the overall grade using 
the midterm and the final grades as inputs""")

midterm = int(input("Enter Midterm grade: "))
final = int(input("Enter Final grade: "))
grade = midterm * .4 + final * .6

print("Overall grade is:", grade)

#    Question 4
help('modules')  #Display all modules.
import _random   #to call the module.
help(_random)    #to view the module with some description.
import email
help(email)
import poplib
help(poplib)

#	Question 5
from math import sqrt
print("""Program to calculate the area of a triangle
using 3 inputs from the user""")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
s = (a + b + c) / 2
area = sqrt(s * (s-a) * (s-b) * (s-c))

print("The area of the triangle is:", area)

#	Question 6
from math import pi
print("Sample input n=3")
n=3
r = n/4
cube = n**3
marbles = 4/3 * (pi * r**3)
marbles_in_cube = cube // marbles
print("Output would be:", marbles_in_cube) #The output should be the same for all inputs

#	Question 7
celsius_temp = int(input("Enter the Celsius temperature you would like to convert: "))
fahrenheit = celsius_temp * 1.8 + 32
kelvin = celsius_temp  + 273.15
reaumur =  celsius_temp * 0.8
rankine = celsius_temp * 1.8 + 32 + 459.67

print (f"fahrenheit: {fahrenheit} \nkelvin: {kelvin} \n\
reaumur: {reaumur} \nrankine:  {rankine}")
            