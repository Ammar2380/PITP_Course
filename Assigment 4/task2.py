
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore Swap → a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After Swap  → a = {a}, b = {b}")
print("\n✅ Values swapped successfully using arithmetic operators!")