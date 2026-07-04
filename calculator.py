a = float(input("First number: "))
op = input("Operator (+, -, *, /,%,//,**): ")
b = float(input("Second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print("Error" if b == 0 else a / b)
elif op == "%":
    print("Error" if b == 0 else a % b)
elif op == "//":
    print("Error" if b == 0 else a // b)
elif op == "**":
    print(a ** b)
else:
    print("Invalid operator")
