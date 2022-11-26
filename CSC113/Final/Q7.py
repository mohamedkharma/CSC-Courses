#	Name: Mohamed Kharma
#	Final Exam

# ========================================================================
# Question 7
print('|Question 7|')
print('''Python3 function to perform the Cartesian product of two sets.
If any set is left empty, an error will rasie by the class 'EmptySet'.\n''')

class EmptySet(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return self.err

def cartesian_product(set1, set2):
    if len(set1) == 0 or len(set2) == 0:
        raise EmptySet("Invalid Input! You can't have an empty set.")
    else:
        output = [(i, j) for i in set1 for j in set2]
        print(output)


flag = 0
while flag == 0:
    try:
        a = input("Enter set1 values separated by spaces: ")
        set1 = a.split()
        for i in set1:
            i = int(i)
        b = input("Enter set2 values separated by spaces: ")
        set2 = b.split()
        for i in set2:
            i = int(i)
        cartesian_product(set1, set2)
        flag = 1
    except Exception as error:
        print(error)
        flag = 0

# ========================================================================