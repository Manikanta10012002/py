for i in range(1,101):
    
    print(i)
    
# task-2
sum = 0
for i in range(1,101):
    print(i) 
    sum += i
    print(sum)   
# task-4
#  num1 = int(input("Enter the number : "))

    
 # medium level task-3
#56723 => o/p => '56723' =>'32765'
#approach 2 =>
num = 12321
rev_num=0
digit_sum =0
count=0
num1=num
while num1!=0:
    rem = num1 %10
    digit_sum += rem
    rev_num = rev_num *10 +rem
    num1 = num1 // 10
    count+=1
print(rev_num)
print(digit_sum)    
print(count)
if rev_num == num:
    print("Palindrome")
else:
    print("Not a palindrome")    

