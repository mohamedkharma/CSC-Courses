#	Name: Mohamed Kharma
#	Midterm Exam

# ========================================================================
# Question 1
print('''Q1: Python3 function to compare each line of two files, character by character, and
if there is a match of the characters, create a variable representing the similarity between
the lines of each file.\n ''')
def compare_files(filename1,filename2):
    f1 = open(filename1,"r")
    f2 = open(filename2,"r")
    f1.read()
    f2.read()
    temp1 = f1.tell()
    temp2 = f2.tell()
    f1.seek(0)
    f2.seek(0)
    similarity = ''
    while ((f1.tell() != temp1) or (f2.tell() != temp2)):
        line1 = f1.readline()
        line2 = f2.readline()
        line1_size = len(line1)
        line2_size = len(line2)
        if len(line1) < line2_size:
            for i in range(0,line1_size):
                if line1[i] == line2[i]:
                    similarity += line1[i]
        else:
            for i in range(0,line2_size):
                if line1[i] == line2[i]:
                    similarity += line2[i]
    f1.close()
    f2.close()
    similarity = similarity.split()
    similarity = ''.join(similarity)
    print(f"The similarity between the two files is: {similarity}")

compare_files('A.txt','B.txt')
# ========================================================================
# Question 2
print('''\nQ2: Python3 function to exchange the first n words in the second line with
the last n words in the last line and write the change back to the same file\n. ''')
def exchange_words(line,n):
  second_line = line[1].split()
  last_line = line[-1].split()

  edited_second_line = last_line[-n:] + second_line[n:]
  edited_last_line = last_line[:-n] + second_line [:n]
  write_to_file(edited_second_line,edited_last_line)

def write_to_file(edited_second_line,edited_last_line):  
  second_str = ' '.join(edited_second_line) + '\n'
  last_str = ' '.join(edited_last_line)  
  F = open('Julius Caesar.txt','r')
  data = F.readlines() 
  F.close()
  fwrite = open('Julius Caesar.txt','w')
  for line in range(len(data)):
    if line == 1:
      fwrite.write(second_str)
      continue
    if line == (len(data) - 1):
      fwrite.write(last_str)
    else:
      fwrite.write(data[line])  

n = int(input('enter the number of words to exchange: '))	#Get the n value 

with open("Julius Caesar.txt") as file:	#Read the content of the file
  data = file.readlines()

exchange_words(data,n) #Call the function exhange 
print("Files words has been successfully exchanged")
# ========================================================================
# Question 3
print('''\nQ3: Python3 function to create a 2D list and another function to project it \n. ''')
def projection(list, a):
    new_list = []
    list_size = len(list)
    if(list_size >= len(a)):
        for i in a:
            new_list.append(list[i-1])
    print(new_list)


def twoD(I):
    i = 0
    twoD = []
    while i < len(I):
        twoD.append(I[i:i+2])
        i = i + 2
    print(twoD)

L= [1, 2.09, 3, 4, 5, 6, 'a', 8, 9, 10.14, 11, 'b']
J= {1, 2, 7}
twoDlist = twoD(L)
projection(L,J)

# ========================================================================
# Question 4
print('''\nQ4: to randomly shuffle the elements of 2D list 
and write it back to the file with that particular order.\n. ''')
import random
def shuffle2DList(filename):
	mainlist = [] 	# A list to store content of file
	file = open(filename,'r')	# open file in read mode
	F = file.read().splitlines()
	index = 0	#to count the elements
	for i in range(0,3):	# reading every line 
		l = []
		for j in range(0,4):
			l.append(int(F[index]))	  #insert each line in List
			index += 1
		mainlist.append(l)
	file.close()
	print("File content BEFORE shuffling the numbers: \n")
	for rows in mainlist:
		for columns in rows:
			print(columns, end= ' ')
		print('')

	print("\nFile content AFTER shuffling the numbers: \n")
	random.shuffle(mainlist)	# randomly shuffle the list
	for rows in mainlist:
		for columns in rows:
			print(columns, end= ' ')
		print('')

	file = open(filename,'w')	# open file in read mode
	for rows in range(0,3):	# reading every line 
		for columns in range(0,4):
			file.write(str(mainlist[rows][columns])+'\n')
	file.close()
  
shuffle2DList('q4.txt')
# ========================================================================
# Question 5
#using print only once with no tripple qoutations (''')
print("**\n*\n****\n***\n******\n*****\n********\n*******\n**********") 
# ========================================================================
# Question 6
#using print only once with no tripple qoutations (''')
print("*\n**\n***\n***\n****\n*****\n****\n*****\n******\n*******\n*****\n******\n*******\n********\n*********\n")
# ========================================================================
# Question 7
print('''\nQ7: Python3 function to apply caesar shifting to any text file.\n. ''')
word =  input("Enter the word you like to shift: ")
num = int(input("Enter the value of n: "))

def caesar_shift(word, num):
    result = ''
    for i in word:
        # Comparing if the char is special symbol
        if i not in ['.',' ','/',';',',','"','\'']:
            result += chr(((ord(i) - ord('a') + num)% 26) + ord('a'))
        else:
            result += i 
    return result 
print(caesar_shift(word, num))
# ========================================================================
# Question 8
print('''\nQ8: Python3 function to to compare every prefix of a string X to every
element of string Y.\n. ''')

def find_prefix(stringX):
  myset = set() 
  str_len = len(stringX)
  for i in range(0,str_len): 
    for j in range(i+1,str_len): 
      myset.add(stringX[i:j]) 
  return myset

def comperaring(stringY,p):
  myset2=set() 
  for i in p:
    if i in stringY:
      myset2.add(i) 
    mylist=list(myset2)
    mylist.sort() 
  print(mylist) 
  mylist2=list(myset2) 
  mylist2.sort(reverse=True) 
  print(mylist2) 

stringX=input("Enter string X: ")
stringY=input("Enter string Y: ")
p=find_prefix(stringX)

comperaring(stringY,p)

# ========================================================================
