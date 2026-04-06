dic1={
    "apple":"saib",
    "mango":"aam",
    "grapes":"angoor",
    "banana":"kela",
    "mcd":"mcdonalds"
}
b=input("enter a word to see its meaning").lower()

if b in dic1:
    print(f"meaning is {dic1[b]}")
else:
    s = input("this fruit is not available in dictionary do u want to add it: ")
    if s == 'yes':
        
        h = input("add  meaning: ")
        dic1.update({b:h})
print(dic1)

dic2 = {}

user = input("enter your username: ")
password = input("enter your password: ")

dic2.update({user: password})

print(dic2)

login_user = input("enter your username: ")
login_password = input("enter your password: ")

if login_user in dic2 and dic2[login_user] == login_password:
    print("login successfully")
else:
    print("invalid username or password")





if login_user in dic2 and dic2[login_user] == login_password:
    print("quiz starting now")

    z=0
    a=input("Q1 Name the city which is capital of Pakistan")
    if a.lower()=="islamabad":
        print("Correct")
        z+=1
        print(f"you got {z} point")
    
    else:
        print("wrong")
        z-=1
        print(f"you got {z} point")
        
    b=input("Q2 Who is the founder of Pakistan?")
    if b.lower()=="quide azam":
        print("correct")
        z+=1
        print(f"you got {z} point")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} point")
        
    c=input("Q3 in which year Pakistan got independence?")
    if c.lower()=="1947":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    d=input("Q4 Which day comes after Friday?")
    if d.lower()=="saturday":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
    e=input("Q5 What do we use to open a lock?")
    if e.lower()=="key":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
    
    f=input("Q6 What is the color of water?")
    if f.lower()=="colorless":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    g=input("Q7 Which animal says meow?")
    if g.lower()=="Cat":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
    
    h=input("Q8 What gas do tree need to breathe?")
    if h.lower()=="carbondioxide":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    i=input("Q9 What is the color of sky?")
    if i.lower()=="blue":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    j=input("Q10 Which insect has worst aerodynamics?")
    if j.lower()=="bumble bee":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    percentage = (z / 10) * 100
    print(f"Your percentage is: {percentage}%")

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Your Grade is: {grade}")
    print(f"You got {z} out of 10 questions correct.")
    print("congratulations! you have completed the quiz.")
else:
    print('invalid password')





