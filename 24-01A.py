# Write a Python program to check if a given number is odd or even.
num1=int(input("Enter the input value:"))
if (num1%2==0):
    print("The given number is Even number")
else:
    print("The given number is Odd number")

 # How do you round a floating-point number to 2 decimal places in Python?

num2=5.90894
x= round(num2,2)
print(x)     

# Write a program to add two complex numbers and print the result.
a=3+6j
b=9+19j
print(a+b)
print(type(a))
# How do you find the first and last character of a given string?
str1=str(input("Enter the String"))
print(str1[0])
print(str1[len(str1)-1])
#How do you add and remove elements from a list in Python?
list1=[0,1,2,3,4,5]
list2=["mani","sai","pant"]
list1[2]=4
x=list1+list2
list2=['mani','sai']
y=list1+list2
print(x)
print(y)
# Write a Python program to check if an element exists in a tuple.
tuple1=(1,2,3,4,2,4,"mani")
x ="mani"
if x in tuple1:
    print("x is existing in the tuple1")
else:
    print("x is not existed in the tuple1")
# Write a Python program to remove duplicate elements from a list using a set.
my_list=[0,1,2,5,4,5,6,7]
# Removing duplicates using a set
unique_list = list(set(my_list))

print("Original list:", my_list)
print("List after removing duplicates:", unique_list)

     
