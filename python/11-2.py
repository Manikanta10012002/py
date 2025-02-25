#Functions
#function is a block of code which runs when ever you call it
#parameters and arguments
#function defination->parameters
#function call -> arguments
#postional arguments
#keyword arguments
#default arguments
#syntax of Function
#return statements 
def example_function(a,b,r,pie=3.14):
    print("mani")
    print("srinivas")
    print("padma")
    print("kumar")
    print("soumya")
    print(a)
    print(b)
    if 1>2:
      return a * b
    print(pie*r*r)
    print(pie)
#someother operation
# example_function(12,11)
# example_function(2,4)
example_function(a=5,b=3,pie=9.12,r=3)
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    
    return "odd"    
print(even_or_odd(47))        

