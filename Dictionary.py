a={
    "apple":"saib",
    "mango":"aam",
    "grapes":"angoor",
    "banana":"kela",
    "mcd":"mcdonalds"
}
b=input("enter a word to see its meaning").lower()

if b in a:
    print(f"meaning is {a[b]}")
else:
    s = input("this fruit is not available in dictionary do u want to add it: ")
    if s == 'yes':
        
        h = input("add  meaning: ")
        a.update({b:h})
print(a)
