#	Name: Mohamed Kharma
#	Final Exam

# ========================================================================
# Question 1
import random

def tables_values(n):
  values = [0.0, 1.0] + [round(random.random(), 3) for x in range(n - 1)] 
  values.sort()
  return [round(values[i+1] - values[i] , 3) for i in range(n)]

print('|Question 1|')
print('''Python3 program to distribute random probability values to Table1 and Table2.
The sum of each table is 1.\n''')
n = int(input("Enter the size you would like the tables to have: ")) 
print('Table1:') 
print(tables_values(n)) 
print('\nTable2:') 
print(tables_values(n)) 
# ========================================================================
