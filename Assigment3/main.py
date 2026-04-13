import time

def my_decorator(func):
    def wrapper():
        print(" starting level ")
        result = func()
        print(" level done ")
        return result
    return wrapper

def level1():
    print("LEVEL 1 - Crack the Login")

    try:
        file1 = open("passwords.txt", "r")
        all_lines = file1.readlines()
        file1.close()
    except:
        print("couldnt find the passwords file")
        return False

    passwords = []
    for line in all_lines:
        passwords.append(line.strip())

    tries = 3
    while tries > 0:
        print("chances left:", tries)
        user_guess = input("enter the password: ")
        user_guess = user_guess.strip()

        if user_guess in passwords:
            print("correct!! moving to next level...")
            return True

        print("wrong password")
        tries = tries - 1

    print("you ran out of tries, level failed")
    return False


def level2():
    print("\nLEVEL 2 - Trace the Hidden Keyword")

    try:
        myfile = open("clue.txt", "r")
        the_key = myfile.read()
        myfile.close()
    except:
        print("couldnt open clue file")
        return False

    the_key = the_key.strip()

    print("you have 30 seconds to type the keyword from the file!!")
    t1 = time.time()
    ans = input(">> ")
    t2 = time.time()

    ans = ans.strip()
    total = t2 - t1

    if ans != the_key:
        print("wrong word, failed")
        return False

    if total > 30:
        print("too slow!! you took", total, "seconds")
        return False

    print("nice!! you did it in", total, "seconds")
    return True


@my_decorator
def level3():
    print("\nLEVEL 3 - Decode the Cipher")

    try:
        f = open("encrypted.txt", "r")
        text = f.read()
        f.close()
    except:
        print("missing encrypted file")
        return False

    real_msg = ""
    i = 0
    while i < len(text):
        letter = text[i]
        real_msg = real_msg + chr(ord(letter) - 1)
        i = i + 1

    print("scrambled message:", text)
    ans = input("what do you think it says? ")

    if ans.lower() == real_msg.lower():
        print("yess you got it!!")
        return True

    print("nope wrong, the answer was:", real_msg)
    return False


def level4():
    print("\nLEVEL 4 - Defuse the Bomb")
    print('riddle: "I speak without a mouth and hear without ears. What am I?"')

    tries = 3
    while tries > 0:
        print("chances left:", tries)
        guess1 = input("your answer: ")
        guess1 = guess1.strip().lower()

        if guess1 == "echo":
            f = open("bomb.txt", "w")
            f.write("Bomb defused successfully!")
            f.close()
            print("Bomb defused successfully!!")
            return True

        print("wrong try again")
        tries = tries - 1

    f = open("bomb.txt", "w")
    f.write("Bomb exploded!")
    f.close()
    print("BOOM!! Bomb exploded!")
    return False


def level5():
    print("\nLEVEL 5 - Final Firewall")
    print("there is a 3x3 grid below, find the weak point")

    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    d = 0
    while d < len(grid):
        print(grid[d])
        d = d + 1

    try:
        r = int(input("enter row (1-3): "))
        c = int(input("enter col (1-3): "))
    except:
        print("thats not a number")
        return False

    weak = (2, 2)

    if r == weak[0] and c == weak[1]:
        print("firewall breached!! YOU WIN THE GAME!!")
        return True

    print("wrong coordinates, firewall held strong")
    return False


print(" Hacker Simulator Starting ")
print()

res1 = level1()

if res1 == True:
    res2 = level2()

    if res2 == True:
        res3 = level3()

        if res3 == True:
            res4 = level4()

            if res4 == True:
                res5 = level5()

                if res5 == True:
                    print()
                    print("MASTER HACKER STATUS ACHIEVED!! you beat the whole game")