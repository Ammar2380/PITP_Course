l = []
a = int(input("how many friends do u have: "))
for i in range(a):
    one  = input("enter your freind name: ")
    two  = input("enter your freind's  father name: ")
    frend_list = l.append(one)
    frend_list = l.append(two)
print(l)
for k in range(a):
    check = input("if u want to chek add your frend name: ")
    check_father = input("if u want to chek add your frend father name: ")
    if check == l & check_father == l:
        print(f'yes you have that frend {check}{check_father}')
    elif check == 'no':
        break
    else:
        add_new = input("this person is not in u r freind list do u want to add this frend: ")
        if add_new == 'yes':
                l.append(check)
                l.append(check_father)
                print("congrats u have added new frend.....")
                print(l)
        elif add_new == 'no':
                break
    


