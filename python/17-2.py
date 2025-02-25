#decorators
# decorators are also a functions
def example_decorator(func):
    def wrapper():
        print("check A4 sheets")
        print("check cartridge")
        func()
        print("Thank you")
    return wrapper

def printer():
    print("printing in  progress....")  
printer()   
@example_decorator
def adding():
    print("Hello world !") 
adding()    
