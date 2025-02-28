# a.  Easy Questions: 
# 1.	Write a program to check if a given number is positive,  negative, or zero.

num1 =int( input("Enter the number:") )

if num1==0:
    print("Zero")
elif num1 > 0:
    print("postive")
else:
    print("Negative")       
# 2.Determine if a number is odd or even.  
num2 =int(input("Enter the number"))
if num2 % 2 ==0:
    print("Even")
else:
    print("Odd")
# 3. Check if a person is eligible to vote (age >= 18).
user_age = int (input("Enter the user_age :"))
if (user_age>=18):
    print("Eligible to vote")
else:
    print("Not Eligible")    
# 4.  Write a program to find the greatest of two numbers. 
num3=float(input("Enter the first number:"))
num4=float(input("Enter the second number"))
if num3>num4:
    print("Greatest number is :",num3)
elif num3<num4:
    print ( "Greatest number is:",num4)    
else:
    print("equal numbers")    
# # 5. Print "Pass" if a student scores more than 40 marks;  otherwise, print "Fail." 
num5=float(input())
score = "pass" if num5 >40 else "fail"
print(score) 
# # 6.Write a program to display the day of the week based on a  number input (1 for Monday, 2 for Tuesday, etc.). 
day=int(input("Enter the day :"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednessday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Enter day is invalid")       
# 7.Implement a simple calculator to perform addition,  subtraction, multiplication, and division.
choice=int(input("enter the choice value (1/2/3/4)")) 
input1=float(input("enter the value :"))        
input2=float(input("Enter the value :"))

if choice==1:
    print("add:",input1+input2)
else:
    if choice==2:
        print("sub :",input1-input2)    
    else:
        if choice==3:
            print("Mul :",input1*input2)
        else:
            if choice==4:
                print("Division: ",input1/input2)
            else:
                print("Invalid please enter the valid choice")    
# 8.Write a program to display the name of a month based on  the month number (1 for January, 2 for February, etc.).  
month=int(input("Enter the month number :"))  
if month==1:
    print("1. january")     
else:
    if month==2:
        print("2. February")
    else:
        if month==3:
            print("3. march")
        else:
            if month==4:
                print("4. April")
            else:
                if month==5:
                    print("5. May")    
                else:
                    if month==6:
                        print("6. june")
                    else:
                        if month==7:
                            print("7. July")
                        else:
                            if month==8:
                                print("8. August")
                            else:
                                if month==9:
                                    print("9. Septmeber")  
                                else:
                                    if month==10:
                                        print("10. October")
                                    else:
                                        if month==11:
                                            print("11. novemeber")
                                        else:
                                            if month==12:
                                                print("12. December")
                                            else:
                                                print("invalid please enter the valid number :")   
#b.  Medium Questions: 
#1.	Write a program to find the greatest of three numbers
n1=float(input("Enter the n1 number:"))
n2=float(input("Enter the n2 number:"))
n3=float(input("Enter the n3 number:"))
if n1>n2 and n1>n3 :
    print("The greatest number is",n1)
else:
    if n2>n1 and n2>n3:
        print("The greatest number is",n2)
    else:
        if n3>n1 and n3>n2:
            print("The greatest number is",n3) 
        else:
            print("Please the valid numbers")     
# 2. Check if a year is a leap year.     
year=int(input("Enter the year"))
if year % 4 == 0 or year % 100==0 and year % 400 ==0 :
    print("Leap year") 
else:
    print("Not a Leap Year")   
# 4. Calculate the grade of a student based on the marks they  score: 
#i.	90-100  : Grade A 
#ii.	80-89  : Grade B 
#iii.	70-79  : Grade C 
#iv.	<70  : Fail. 
marks=float(input("Enter the marks:"))
if marks >=90:
    print("Grade A")
elif marks >=80:
    print("Grade B")    
elif marks >= 70:
    print("Grade C")    
else:
    print("Fail")    
# 5. Write a program to check if three sides length form a valid  triangle. 
side1=float(input("Enter the side a value:"))
side2=float(input("Enter the side b value:"))
side3=float(input("Enter the side c value:"))
if side1+side2>side3 or side2+side3>side1 or side1+side3>side2 :
    print("It is a valid Triangle")
else:
    print("Not a valid Triangle")    
              
                                                                                                       




 