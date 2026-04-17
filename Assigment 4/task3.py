import pandas as pd

print(" User Details Form")

name = input("Enter your Name: ").strip()

while True:
    try:
        age = int(input("Enter your Age: "))
        if age <= 0:
            print("Age must be positive number!")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number for age.")

email = input("Enter your Email address: ").strip()

data = {
    "Name": [name],
    "Age": [age],
    "Email": [email]
}

df = pd.DataFrame(data)

df.to_excel("user_details.xlsx", index=False)

print("\n Details saved successfully to 'user_details.xlsx' !")
print("You can open the file now.")