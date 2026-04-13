i = 0
while i < 50:
    if i%5==0 & i%3==0:
        print(i,"ding dong")  
        i+=1  
    if i%3==0:
        print("ding")
    elif i%5==0:
        print("dong")
        i+=1
i = 0
for i in  range(50):
    if i%5==0 & i%3==0:
        print("ding dong")   
    if i%3==0:
        print("ding")
    elif i%5==0:
        print("dong")
       

guess_num = 50

times_guess = int(input("how many guesses you want: "))
i=0
for i in range(times_guess) :
    user_input = int(input("guess the number: "))
    if user_input ==  guess_num:
        break 

count = 0 
while count <=7:
    print(count)
    count+=1

cube = 1
d = 1
while d <= 4:
    print(cube**3)
    d+=1
    cube+=1

square = 2
d = 1
while d <= 7:
    
    print(square**2)
    d+=1
    square+=1

sum_all = 0
sum_even = 2
d = 1
while d <= 10:
    if sum_even%2==0:
        sum_all+=sum_even
        print(sum_all)
    d+=1
    sum_even+=1
        
   


