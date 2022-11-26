#	Name: Mohamed Kharma
#	Lab Assignment 2

# ========================================================================
# Question 1

print('''Program to check a perfect number is a positive integer 
that is equal to the sum of its proper positive divisors\n''')
# This function is to find perfect num
def isPerfectNumber(num):
    totalNums = 0
    for i in range(1,num): # begin dividing with 1 because 0 will result in error.
        if num % i == 0:
            totalNums += i
    return totalNums == num    # returns true if totalNums == num

    
flag = True
while flag:     #keep running as long as its true 
        try:
            num = int(input("Enter a number to check whether its a perfect or not: "))
            if isPerfectNumber(num) == True:
                    print(f"{num} is a perfect number!")
            else:
                    print(f"{num} is not a perfect number!")

            print("\nWould you like to try different number?")
            select = str(input("Enter 'Yes' to try again or 'No' to quit: ")).upper() # checks user selected choice to continue
            while not(select[0] == 'Y' or select[0] == 'N'):
                    select = str(input("Try entering either 'Yes' to try again or 'No' to quit: ")).upper() # checks user selected choice to continue
            if (select[0] == 'N'):
                    flag = False
            else:
                    flag = True
        except ValueError:
                print(f"{num} is not an integer. Try entering an integer")

# =======================================================================
# Question 2

print("""\nThis program will find all prime numbers between two inclusive integer numbers.
Prime numbers will be displayed to the screen and saved in 'primes.txt' file.""")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

file = open('primes.txt', 'w')  # 'w' allows us to overwrite the numbers inside prime.txt file
print(f"Prime numbers between {num1} and {num2} are:")
for i in range(num1, num2 + 1):	# Go left by one becasue num2 is inclusive
   
   if i > 1:	# all prime numbers starts after 1
       for j in range(2, i): 	 # i is exclusive
           if (i % j) == 0:
               break
       else:
           print(i)
           file.write(str(i) + '\n') 	# write i to prime.txt file
file.close()              

# ========================================================================
# Question 3

print("\nThis program is going to check whether the 3 points on the coordinate plane creates a triangle or not.")
def get_coordinates():
        x = float(input("Enter the coordinate of x: "))
        y = float(input("Enter the coordinate of x: "))
        return x,y

# Function to check that create a triangle 
def is_triangle(x1, y1, x2, y2, x3, y3): 
        
        #find area of triangle
        area = ((x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2)

        if area < 0:    # if area is negative
                area *= -1  # returns positive area
        
        if area != 0: # if area doesn't equal zero, then its a triangle
                print(f'The coordinates does creates a triangle.')
        else:
                print(f'The coordinates does NOT create a triangle.')
        return area

flag = True
while (flag):
	try:
		print("First point (x1,y1)")
		x1,y1 = get_coordinates()
		print("\nSecond point (x2,y2)")
		x2,y2 = get_coordinates()
		print("\nThird point (x3,y3)")
		x3,y3 = get_coordinates()
		
		area = is_triangle(x1,y1,x2,y2,x3,y3)

		print("\nWould you like to try again?")
		choice = str(input("Enter 'Yes' to try again or 'No' to quit: ")).upper() # checks user choice to continue
		while not (choice[0] == 'Y' or choice[0] == 'N'):                                                   
			choice = str(input("Please try entering 'Yes' or 'No' as an input: ")).upper()
		# Checks if user says No, so we exit the while loop
		if choice[0] == 'N':
			flag = False 
		else:
			True     # Ternary operator

	except ValueError: # checks if the user entered any invalid inputs 
		print("Your input is not a valid. Please enter an integer only!")

# ========================================================================
# Question 4
# NOTE: I tried running my code in Linux and it works fine, however in windows it won't work unless
# 		I included -> encoding = "utf-8" next to the file.
#		For example file1 = open('quotes1.txt','r', encoding = "utf-8") will work in windows but 
#		I didn't used it since we didn't go over it in lectures.
#		My code should work fine in Linux.
file1 = open('quotes1.txt','r') #open the file using 'r' to read it
file2 = open('quotes2.txt','w') #create a new file and over write it using 'w'
lines = file1.readlines() #return all new lines in file1
linesNum = len(lines)
for i in range(linesNum): # a loop to remove extra lines
    if lines[i] != '\n':
        file2.write(lines[i])
file1.close()
file2.close()

# ========================================================================
# Question 5

def lines_format():
	inputs = F.read()
	L = inputs.split("\n") 

	storge_list=[] # to store the lines index 
	for i in L:
		# remove all the empty line from the list
		if i != "":
			storge_list.append(i) # add only the lines that are not empty

			num = len(storge_list) # calculate the number of lines
			# check whether number num is prime or not
			flag = 0
			if num > 1:
				for i in range(2,num):
					if num%i == 0:
						flag=1
						break
				F.seek(0)  # moving the pointer to beginning of the file


				F.truncate()  # needed to delete the old inputs

	# if number if prime, then we just write all inputs without new lines.
				if flag == 0:
					for i in L:
						F.write(i)

	# if number is not prime, then we just add tab instead a new line.
				else:
					for i in L:
						F.write(i+"\t")
	F.close()

F = open("TestPrimeLines.txt","r+")
lines_format()
F = open("TestNonPrimeLines.txt","r+")
lines_format()

# ========================================================================
# Question 6

print("This program will trims one character from end of any string and print until k characters")
def word_fadding(word, k):
    print(word)    #print the original string.

    length=len(word) #number of characters in the word
    n=length-k  #(number of characters in the word) - k indenx
    for x in range(n):
        word=word[:-1]  # going in reverse
        print(word)   #print new string after the remove of last character in each iteration.
# string and store the word.        
word = input("Enter any string: ")
# k indicates how many characters are left
k = int(input("Enter an intger to indicate at what index you wolud like the program to stop: "))

word_fadding(word,k)

# ========================================================================
