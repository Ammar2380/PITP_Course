# # # a = [1,2,3,4,5,6,7]
# # # b = map(lambda x:x%2==0,a)
# # # print(list(b)) 
# # a = [1,2,3,4,5,6,7]
# # b = filter(lambda x:x%2==0,a)
# # print(list(b)) # only those who are even like name filter

# # # map : works like for loop visit each
# # # filter : filter data according to condition

# # # decorator 
b = input("enter your pass: ")

def deco(a):
    def deco1():
        pas = "sds"
        if b == pas:
            print("welcome to the colgate company")
            a()
            print("made by me")
        else:
            print("Wrong password")
    
    return deco1   

@deco
def abc():
    print("data science")

abc()

# # a=lambda x,y:x%2==0 and or
# # b=2
# # c=3
# # print(a(b))
# a=[1,2,3,4,5,6]
# b=filter(lambda x:x<5,a)
# print(list(b))
# # map
# # filter

# # decorator

# a = input("enter ur password: ")
# def deco(a):
#     def deco1(*args):
#         print("welcome to the colagate company")
#         a(*args)
#         pas = "acc_pass"
#         print("made by arham")
#     return deco1



# if a == @deco
# def abc(a,b):
#     print(a+b)
# abc(3,3)