def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot perform modulus with zero!"

def exponent(x, y):
    return x ** y

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter the operation (+, -, *, /, %, **): ")

    if operation == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == '-':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '*':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '/':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif operation == '%':
        print(f"{num1} % {num2} = {modulus(num1, num2)}")
    elif operation == '**':
        print(f"{num1} ** {num2} = {exponent(num1, num2)}")
    else:
        print("Invalid operation entered!")
