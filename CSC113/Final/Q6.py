#	Name: Mohamed Kharma
#	Final Exam

# ========================================================================
# Question 6
import random
listA_rows = random.randint(1,10)
listA_columns = random.randint(1,10)
listA = [[random.randint(0,100) for i in range(listA_columns)] for j in range(listA_rows)]

listB_rows = random.randint(1,10)
listB_columns = random.randint(1,10)
listB = [[random.randint(0,100) for i in range(listB_columns)] for j in range(listB_rows)]

print("|Question 6|")
print('Python3 program to check if we can multiply these two lists as matrices\n')
print(f'''Random 2D List A with columns x rows is: {len(listA)} x {len(listA[0])} 
and list B with columns x rows is: {len(listB)} x {len(listB[0])}\n''')

if (len(listA[0]) == len(listB)) or (len(listA) == len(listB[0])):
  print("We can multiply these two lists as matrices.")      
else:
   print("We can NOT multiply these two lists as matrices.")
# ========================================================================