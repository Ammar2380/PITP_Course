x="12345"
y=input("enter your password")
if y==x:
    print("starting quiz")
    z=0
    a=input("Q1 what is the capital of Pakistan")
    if a.lower()=="islamabad":
        print("Correct")
        z+=1
        print(f"you got {z} point")
    
    else:
        print("wrong")
        z-=1
        print(f"you got {z} point")
    b=input("Q2 what is the national language of Pakistan")
    if b.lower()=="urdu":
        print("correct")
        z+=1
        print(f"you got {z} point")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} point")
        
    c=input("Q3 what is the largest ocean in the world")
    if c.lower()=="pacific":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    d=input("Q4 how many continents are there in the world")
    if d.lower()=="seven" or d=="7":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
    e=input("Q5 what is the currency of Pakistan")
    if e.lower()=="rupee":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
    
    f=input("Q6 Which animal is known as the King of the Jungle?")
    if f.lower()=="lion":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    g=input("Q7 How many days are there in a week")
    if g.lower()=="7":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
    
    h=input("Q8 What gas do humans need to breathe?")
    if h.lower()=="oxygen":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    i=input("Q9 Which organ pumps blood through the human body?")
    if i.lower()=="heart":
        print("correct")
        z+=1
        print(f"you got {z} points")
    else:
        print("wrong")
        z-=1
        print(f"you got {z} points")
        
    j=input("Q10 Which animal says meow")
    if j.lower()=="cat":
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
    print("invalid password")
    





