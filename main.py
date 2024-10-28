print('BasicCalculator')

firstNumber = int(input("What is your first number? "))
operator = input("What is the operator? ")
secondNumber = int(input("What is your second number? "))

if operator == "-":
    result = firstNumber - secondNumber
if operator == "+":
    result = firstNumber + secondNumber
if operator == "*":
    result = firstNumber * secondNumber
if operator == "/":
    result = firstNumber / secondNumber
if operator == "%":
    result = firstNumber % secondNumber

print(f"Result: {result}")