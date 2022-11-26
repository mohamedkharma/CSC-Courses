# Name: Mohamed Kharma
# Final Exam

# ========================================================================
# Question 5
import math
def right_trangle(x1,x2,x3,y1,y2,y3):
  l1= math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
  l2= math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
  l3= math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
  flag=0
  if (l1*l1+l2*l2==l3*l3):
    flag=1
  elif (l1*l1+l3*l3==l2*l2):
    flag=1
  elif (l3*l3+l2*l2==l1*l1):
    flag=1
  if (flag==1):
    print("\nThe provided points does form a right triangle")
  else:
    print("\nThe provided points does NOT form a right triangle")
  

def equilateral_trangle(x1,x2,x3,y1,y2,y3):
  l1= round(math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)))
  l2= round(math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)))
  l3= round(math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))
  if(l1==l2==l3):
    print("The provided points does form a equilateral triangle")
  else:
    print("The provided points does NOT form a equilateral triangle")

print(' |Question 5| ')
print('''Two Python3 functions. One to check whether the points
entered forms a right triangle and another to check whether the
points entered forms a equilateral triangle.\n''')

x1 = float(input("Enter x-coordinate for point x1: "))
y1 = float(input("Enter y-coordinate for point y1: "))
x2 = float(input("Enter x-coordinate for point x2: "))
y2 = float(input("Enter y-coordinate for point y2: "))
x3 = float(input("Enter x-coordinate for point x3: "))
y3 = float(input("Enter y-coordinate for point y3: "))

right_trangle(x1,x2,x3,y1,y2,y3)
equilateral_trangle(x1,x2,x3,y1,y2,y3)
# ========================================================================
