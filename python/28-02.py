# # prime number 
# num1=int(input("Enter a number to check for prime "))
# #approach 1
# if num1 in[0,1] or num1<0:
#     print("Neither prime nor composite")
# else:
#     count=0
#     for i in range (1, num1+1):
#         if num1 % i ==0:
#             count +=1
#     print("Prime")if count==2 else print("Not prime")            
#Approach 2
# if num1 in [0,1] or num1 < 0:
#     print("Neither prime nor compostie")
# else:
#     spy=True
#     for i in range(2,num1):
#         if num1% i ==0:
#             spy=False
#             print("Not a prime")
#             break
#     if spy:
#         print("prime")  
#Approach 3
#18 - 1,2,3,6,9,18
#22 - 1,2,11,22
#39 - 1,3,13,39
#17 - 1,17
#54 - 1,2,3,6,9,18,27,54
#c = a*b (a=c, b=1)
#c = a*b (a=c/2,b=2) 
# if num1 in [0,1] or num1 < 0:
#     print("Neither prime nor compostie")
# else:
#     spy=True
#     for i in range(2,num1 //2+1):
#         if num1% i ==0:
#             spy=False
#             print("Not a prime")
#             break
#     if spy:
#         print("prime")    
#Approach 4
#64
#1*64=64
# 2*32
# 4*16
# 8*8
# 16*4
#32*2
#64*1
# if num1 in [0,1] or num1 < 0:
#     print("Neither prime nor compostie")
# else:
#     spy=True
#     for i in range(2,int(num1**0.5)+1):
#         if num1% i ==0:
#             spy=False
#             print("Not a prime")
#             break
#     if spy:
#         print("prime")    

#Fibonacci Number
# f(n) = f(n-1)+f    
num1=0
num2=1
print(num1)
print(num2)
for i in range(0,13):
    temp =num1+num2
    print(temp)
    num1=num2
    num2 = temp

   
