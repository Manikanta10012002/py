# def sum(a=3,b=6):
#     return a*b
# # def sum(a=4, b=6 , c=9 , d=2):
# #     return a + b - c + d
# sum
#  arguments
# keyword argument
def sum(a,*args):
    res = a
    for k in args:
        res += k
    return res 
sum(2,3,4,5,6,7,8)   
#types of functions
#void function - a function without return statement
#Function with return statements
# void function
# def random_print():
#    print("this is just to print")   
# lambda function- simple , single line , optimization, anony 
lam_example = lambda x,y,z : x*y*z
print(lam_example(2,2,2))
lan = lambda : "mani"
print(lan())
#map (func, iterable)
def square(x):
    return x * x
res_map = map(square,[2,45,90,-4])
print(list(res_map))
res_map1 = map(lambda x : x **3, [1,2,3,4,5])
print(list(res_map1))

    