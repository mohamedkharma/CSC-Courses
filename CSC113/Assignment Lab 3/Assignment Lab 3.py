#	Name: Mohamed Kharma
#	Lab Assignment 3

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
print('''\nQ2: A function that randomly adds either `X' or `Y' to the end of each
line.And another function to show the number of the lines finishing with XX and YY and the ratio of the lines
finishing with `XX' and `YY' / all n-lines.\n''')

import random # Importing module random for generating random numbers

letters = ['X','Y']
countlines = 0

file = open('addxory.txt','w') # Opening the file in write mode
for i in range(1000): # Repeat 1000 times
 
    r = random.randint(0,1) # Generating either 0 or 1
    XorY = letters[r]  # Generating X or Y based on the index generated
    file.writelines( f"This line ends with a random: {XorY}\n") # Write to the file
file.close()

def addXorY(filename):
    letters = ['X','Y']
    file = open(filename,'r') # Open the given text file in read mode
    content = file.readlines()  # Reading all the 1000 lines and storing them
    file.close()

    file = open(filename,'w') # Opening the same file again in write mode
    for line in content: #For each line
        line = line.replace("\n", "")# Remove the newline character
        Idx = random.randint(0, 1)  # Generate either 0 or 1

        # Add either X or Y from list letters based on the random index generated
        line = line + letters[Idx] + "\n"
        # Write the line to the file
        file.write(line)
    file.close()

def show_and_count(filename):
    doubleX = doubleY = 0
    file = open(filename,'r') # Opening the given file
    content  = file.readlines() # Reading all the lines from the file
    # For each individual line read, remove the newline
    for line in content:
        line = line.replace("\n","")
        if (line[-2:] == "XX"):
            doubleX += 1
        elif (line[-2:] == "YY") :
            doubleY += 1

    # Displaying
    print(f"\nNumber of lines that ends with double XX: {doubleX}")
    print(f"Number of lines that ends with double YY: {doubleY}")

    # Calculating the ratio
    ratio = (doubleX + doubleY) / 1000
    print(f"\nRatio of lines ending with XX and YY to total lines: {ratio}")

addXorY("addxory.txt")
show_and_count("addxory.txt")
# ========================================================================
# Question 3
print('''\nQ3: Python3 function to create a 2D list and another function to project it. \n ''')

def twoD(I,J):
    mylist =[] 
    print('\nA 2D list that contain the given values for I:\n')
    for i in range (0,len(I),2): 
            mylist.append(I[i:i+2]) 
    #print the list
    for row in mylist:
        for col in row:
            print (col, end = ' ')
        print('')
    #send to a new function
    projection(J,mylist)

def projection(J,mylist):
    try:   
        for i in J:
            print(f'At index {i}, the coordinates are: ',mylist[i-1])
    except:
        print(f'At index {i}, there is no coordinates because its out of range!\n')

I= [1, 2.09, 3, 4, 5, 6, 'a', 8, 9, 10.14, 11, 'b']
J= {1, 2, 7}   
twoD(I,J)
# ========================================================================
# Question 4
print('\nQ4: Python3 classes for the UML diagram')
class User:
  def __init__(self, userId, password, loginstat):
    self.userId= userId
    self.password= password
    self.loginstat = loginstat
  def verifyLogin():
    pass

class Customer(User):
  def __init__(self,customerName, address, email, creditCard, shipping):
    self.customerName = customerName
    self.address = address
    self.email = email
    self.creditCardInfo = creditCard
    self.shippingInfo - shipping
    self.shopingCart = shopingCart()
    self.Oders = Orders()
  def register():
    pass
  def login():
    pass 
  def updateProfile():
    pass

class shopingCart:
  def __init__(self, cartId, productId, quantity, dateAdded):
    self.cardId = cartId
    self.productId = productId
    self.quantity = quantity
    self.dateAdded = dateAdded
  def addCartItem():
    pass
  def updateQuantity():
    pass
  def viewCartDetails():
    pass
  def checkOut():
    pass

class Orders:
  def __init__(self, orderId, dateCreated, dateShipped, customerName, customerId, status, shippingID):
    self.orderId = orderId
    self.dateCreated = dateCreated
    self.dateShipped = dateShipped
    self.customerName = customerName
    self.customerId = customerId
    self.status = status
    self.shippingId = shippingID
    self.ShippingInfo = ShippingInfo()
    self.oderDetails= OrderDetials()
  def paceOrder():
    pass
  

class OrderDetials():
  def __init__(self, orderId, productId, productName, quantity, unitCost, subtotal):
    self.orderId = orderId
    self.productId = productId
    self.productName = productName
    self.quantity = quantity
    self.unitCost = unitCost
    self.subtotal = subtotal
  def catcPrice():
    pass
    
class ShippingInfo:
  def __init__(self,shippingId, shippingType, shippingCost, shippingRegionId):
    self.shippingId = shippingId
    self.shippingType = shippingType
    self.shippingCost = shippingCost
    self.shippingRegionid = shippingRegionId
  def updateShippingInfo():
    pass

class Administrator(User):
  def __init__(self, adminName, email):
    self.adminName = adminName
    self.email = email
  def updateCatalog():
    pass
# ========================================================================
# Question 5
print('''\nQ5: to randomly shuffle the elements of 2D list 
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
  
shuffle2DList('q5.txt')
# ========================================================================
# Question 6
print('''\nQ6: A 3D list of x rows y columns and z layers (Z x Y x X) will be created where x,y, and z are provided by the user.
The programme creates the 3D list and fills it with random numbers(0-1000) and then a function will divides the 3D list into m 2D lists.
import random''')

x = int(input("Enter number of rows please: "))
y = int(input("Enter number of columns please: "))
z = int(input("Enter number of 2D lists please: ")) #in our case it's m

mylist = []

#this function just returns a random value between 0 and 1000
def random_number():
	return random.randint(0,1000)

#adding z 2D lists with x rows and y columns having random values
for i in range(z):
	mylist.append([])
	  
	for j in range(y):
		mylist[i].append([])
		  
		for k in range(x):
			mylist[i][j].append(random_number())

print(f"\n\n3D {x}x {x}x {x}random number list:-")
print(mylist)

#function that just prints mth 2D list in 3D list
def list3Dto2D(a,m):
	for i in range(m):
		print(a[i])

print("\n\nConverted into m 2D lists:")
list3Dto2D(mylist,z)
# ========================================================================
