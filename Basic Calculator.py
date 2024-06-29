print("Enter Operation you want to perform (+,-,*,/) :")
operation = input()
num1 = float(input("Enter the frist number : "))
num2 = float(input("Enter the second number : "))

if operation == "+" :
    result = num1 + num2
elif operation == "-" :
    result = num1 - num2
elif operation == "*" :
    result = num1 * num2
elif operation == "/" :
    result = num1 / num2
else :
    result = "None"

if result is None :
    print("Invalid")
else : 
    print(f"Your result is : {result}")