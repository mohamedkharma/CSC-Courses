#	Name: Mohamed Kharma
#	Final Exam

# ========================================================================
# Question 4:
import random
class matrix:
  def __init__(mylist,r=0,c=0,matrix=[]):
    mylist.r = r
    mylist.c = c
    mylist.matrix = [[random.randint(0,9) for i in range(mylist.c)] for j in range(mylist.r)]
    
  def rotate_num(mylist,n):
    mylist.n=n
    mylist.newmat=[]  
    mymatrix=mylist.matrix
    if(mylist.n % 4 == 0):
      mylist.new_matrix(mymatrix)
    elif(mylist.n<0):
      for i in range(4-(mylist.n%4)):
        mymatrix=mylist.rotate_martrix(mymatrix)
      mylist.new_matrix(mymatrix)
    elif(mylist.n % 4 > 0 ):
      for i in range(mylist.n % 4):
        mymatrix=mylist.rotate_martrix(mymatrix)
      mylist.new_matrix(mymatrix)

  def orignal_matrix(mylist):
    for i in range(len(mylist.matrix)):
      for j in range(len(mylist.matrix[i])):
        print(mylist.matrix[i][j],end=' ')
      print()

  def new_matrix(mylist,mymatrix):
    for i in range(len(mymatrix)):
      for j in range(len(mymatrix[i])):
        print(mymatrix[i][j],end=' ')
      print()

  def rotate_martrix(mylist,mymatrix):
    if(mylist.n<0):
      
      rotatedlist=[]
      for i in range(len(mymatrix)-1,-1,-1):
        templist=[]
        for j in range(len(mymatrix[i])-1,-1,-1):
          templist.append(mymatrix[j][i])
        rotatedlist.append(templist)
      for i in rotatedlist:
        i.reverse()
      return rotatedlist

    else:
      rotatedlist=[]
      for i in range(len(mymatrix[0])):
        templist=[]
        for j in range(len(mymatrix)):
          templist.append(mymatrix[j][i])
        templist.reverse()
        rotatedlist.append(templist)
      return rotatedlist
 
print('|Question 4|')   
print('''Python3 program to create a random matrix and a function 
to rotate the matrix clockwise or counterclockwise n times and prints it to the screen.\n''')
ob=matrix(3,3)
print('Orignal matrix is:')
ob.orignal_matrix()

print('\nThe new rotated matrix is: ')
ob.rotate_num(1)
# ========================================================================