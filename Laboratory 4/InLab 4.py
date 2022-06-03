# Inlab
'''A. Write a short recursive Python function that finds the minimum and
maximum values in a sequence without using any loops.'''


def Min(S): #function to define the maximum value of the list
    if len(S) == 0: #if the given list is equal to 0
        return None #it will return the value of none
    if len(S) == 1: # if the given list is equal to 1
        return S[0] #it will return a value of 0
    return min(S[0], Min(S[1:])) #returns the minimum value of the given list

def Max(S): #function to define the maximum element of the list
    if len(S) == 0: #if the given list is equal to 0
        return None#it will return the value of none
    if len(S) == 1:# if the given list is equal to 1
        return S[0]#it will return a value of 0
    return max(S[0], Max(S[1:])) #returns the maximum value of the given list

print("A")
print(Max([2, 4, 6, 8, 10]))
print(Min([1, 3, 5, 7, 9]))
print("\n")


'''B. Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction.'''

def multiply(m, n): #defines the function of multiply with parameters of m and n
    if n <= 1: #states that if the value of n is less than or equal to 1
        return m #it will return the value of m
    else:
        result = m + multiply(m, n - 1) #else it will get the value of result which is the value of m
                                        #plus the recursive value of the m and n-1
        return result       #prints the result


print("B")
m = int(input("input the first number (m): ")) #lets the user to input the value of the m
n = int(input("input the second number (n): ")) #lets the user to input the value of the n
print("The product is", multiply(m, n)) #prints the product of m and n
print("\n")

'''C. Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be
snap&stop'''

print("C")
def revString(string): #defines the function revString with the parameter of string
    if len(string) == 0: #if there is no string value it will return the string
        return string
    else:
        return revString(string[1:]) + string[0] #else it recurses and reverses the string characters


a = str(input("Enter the string to be reversed: "))
print(revString(a))
