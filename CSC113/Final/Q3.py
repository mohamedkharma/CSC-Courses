# Name: Mohamed Kharma
# Final Exam

# ========================================================================
# Question 3
def encrypted(lines, s):
  
   original_file=open("original.txt","r")
   encrypt_file=open("encrypted.txt","w")
   mydata=original_file.read()

   for n in range(len(mydata)):
       ascii_val=ord(mydata[n])
       if ((mydata[n].isalpha()) and (mydata[n].isupper())):
           ascii_val=ascii_val+s         
           if ascii_val>90:
               ascii_val=64+(ascii_val-90)  
          
       elif mydata[n].isalpha() and mydata[n].islower():     
           ascii_val=ascii_val-s          
           if ascii_val<97:
               ascii_val=122-(96-ascii_val)
      
       elif mydata[n].isdigit():
           ascii_val=ascii_val-s
           if ascii_val<48:
               ascii_val=57-(47-ascii_val)
      
       encrypt_file.write(chr(ascii_val))      
   original_file.close()
   encrypt_file.close()

def decrypted(file, s): 
   encrypt_file=open("encrypted.txt","r")  
   original_file=open("original.txt","w")
   mydata=encrypt_file.read()

   for n in range(len(mydata)): 
       ascii_val=ord(mydata[n])      
       if mydata[n].isalpha() and mydata[n].isupper():     
           ascii_val=ascii_val-s
           if ascii_val<65:
               ascii_val=90-(64-ascii_val)  
      
       elif mydata[n].isalpha() and mydata[n].islower():
           ascii_val=ascii_val+s
           if ascii_val>122:
               ascii_val=96+(ascii_val-122)  
      
       elif mydata[n].isdigit():
           ascii_val=ascii_val+s
           if ascii_val>57:
               ascii_val=47+(ascii_val-57)  
      
       original_file.write(chr(ascii_val))      
   encrypt_file.close()
   original_file.close()

print('|Question 3|')
print('''Python3 program to encrypt and decrypt a text file using two functions.''')
f1 = open('original.txt','r')
f2 = open('encrypted.txt','r')
lines1 = f1.readlines()
lines2 = f2.readlines()
s = 1 #Change the number of s to shift more or less
encrypted(lines1,s)
decrypted('encrypted.txt',s)

for i in lines2:
    print('When Encrypted: ',i,end='')
for j in lines1:
    print('\nWhen Decrypted: ',j,end='')
f1.close()
f2.close()
# ========================================================================
