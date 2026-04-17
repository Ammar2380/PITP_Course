

print(" Welcome to Login System ")


users = {}


username = input("Create your username: ")
password = input("Create your password: ")

users[username] = password
print("\nAccount created successfully!\n")

login_user = input("Enter your username to login: ")
login_pass = input("Enter your password: ")



if login_user in users and users[login_user] == login_pass:
    print("\nLogin Successful! ")
    print("Starting Quiz...\n")

   

    score = 0

    questions = [
        {
            "question": "Q1: Capital of Pakistan?",
            "options": ["A) Karachi", "B) Lahore", "C) Islamabad", "D) Quetta"],
            "answer": "c"
        },
        {
            "question": "Q2: Founder of Pakistan?",
            "options": ["A) Allama Iqbal", "B) Quaid-e-Azam", "C) Liaquat Ali Khan", "D) Sir Syed"],
            "answer": "b"
        },
        {
            "question": "Q3: Independence year?",
            "options": ["A) 1945", "B) 1946", "C) 1947", "D) 1948"],
            "answer": "c"
        },
        {
            "question": "Q4: Which day comes after Friday?",
            "options": ["A) Sunday", "B) Saturday", "C) Monday", "D) Thursday"],
            "answer": "b"
        },
        {
            "question": "Q5: What opens a lock?",
            "options": ["A) Hammer", "B) Key", "C) Knife", "D) Stick"],
            "answer": "b"
        }
    ]

    #
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)

        ans = input("Enter your answer (a/b/c/d): ").lower()

        if ans == q["answer"]:
            print("Correct \n")
            score += 1
        else:
            print("Wrong \n")

   

    print(" QUIZ RESULT ")
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage}%")

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

    print(f"Grade: {grade}")
    print(" Quiz Completed Successfully!")

else:
    print("\nAccount not found, please create an account ")