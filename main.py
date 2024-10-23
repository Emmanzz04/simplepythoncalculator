# First section of code cover the input variables
Operator = input ("Enter an operator (+ - * /):")
num1 = float(input ("Enter a value:"))
num2 = float(input ("Enter a value:"))

#The provided if statement to display the necessary variables
if Operator == "+":
  result = num1 + num2 
  print(round(result, 3))
elif Operator == "-":
  result = num1 - num2
  print(round(result, 3))
elif Operator == "*":
  result = num1 * num2 
  print(round(result, 3))
elif Operator == "/":
  result = num1 / num2
  print(round(result, 3))
else:
  print(f"This{Operator} is not valid")




