# def myfunction(a,b): # Parameters
#     # a = 'sddd'
#     a = int(input(  "enter a number: "))
#     b = int(input( "enter a number: "))
#     print(a+b)
# myfunction(3,2) # arguments

def sum_function(a,b):

    print(a+b)
 
def sub_function(a,b):
 
    print(a-b)
 
def mul_function(a,b):
  
    print(a*b)
 
def div_function(a,b):
   
    print(a/b)

number1 = int(input("enter your number1: "))
number2 = int(input("enter your number2: "))
operation = input("enter your operation: ")

if operation == '+':
    sum_function(number1,number2)
elif operation == '-':
    sub_function(number1,number2)
elif operation == "*":
    mul_function(number1,number2)
elif operation == "/":
    div_function(number1,number2)