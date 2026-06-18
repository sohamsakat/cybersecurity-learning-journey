# Program 1 — Greeting
name1 = input("Hello there whats you name: ")
print("Welcome to cybersecurity", name1)

#Program 2 — Sum of two numbers Take two numbers as input. Print their sum. Handle the case where user types letters instead of numbers using try/except.
try:
    num1 = float(input("Enter first additive: "))
    num2 = float(input("Enter second additive: "))

    print("Sum= ", num1 + num2)
except ValueError:
    print("Enter correct additive value")


#Program 3 — Even or Odd Take a number. Tell user if it is even or odd.
oddeve = int(input("Enter number for ODD and EVEN: "))
if oddeve % 2 == 0:
    print("EVEN")
else:
    print("ODD")

#Program 4 — Calculator Take two numbers and an operator (+, -, *, /). Perform the operation. If user tries to divide by zero, print a proper error message instead of crashing.

try:
    num3 = float(input("Enter first operand: "))
    num4 = float(input("Enter second operand: "))

    operator = input("Enter the desired operator out of {+, -, *, /}: ")

    if operator == "+":
        print("SUM:", num3 + num4)

    elif operator == "-":
        print("SUBTRACTION:", num3 - num4)

    elif operator == "*":
        print("MULTIPLICATION:", num3 * num4)

    elif operator == "/":
        if num4 == 0:
            print("CANNOT DIVIDE BY ZERO")

        else:
            print("DIVISION:", num3 / num4)

    else:
        print("ENTER VALID OPERATOR")

except ValueError:
    print("Please enter valid numbers.")
    

    

#Program 5 — Vote eligibility Take age as input. If 18 or above print eligible to vote. If below 18 print not eligible and how many years remain.

age = int(input("Enter Your Age: "))

if age >= 18:
    print("YOU ARE ELIGIBLE TO VOTE FOR THE UPCOMING ELECTIONS: ")
else:
    print("TRY AFTER ", 18-age, "years")


#Program 6 — Largest of 3 numbers Take 3 numbers. Find the largest without using max(). Use only if/elif/else.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if num1 >= num2 and num1 >= num3:
        print("Largest number is:", num1)

    elif num2 >= num1 and num2 >= num3:
        print("Largest number is:", num2)

    else:
        print("Largest number is:", num3)

except ValueError:
    print("Please enter valid numbers.")

#Program 7 — Reverse a number Take a number like 1234. Print 4321. Do it mathematically using % and // operators, not by converting to string.
try:
    number = int(input("Enter a number: "))

    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    print("Reversed number:", reverse)

except ValueError:
    print("Please enter a valid number.")
#Program 8 — FizzBuzz Print numbers 1 to 50. If divisible by 3 print Fizz. If divisible by 5 print Buzz. If divisible by both print FizzBuzz. Otherwise print the number.
for number in range(1, 51):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
#Program 9 — Simple login system Hardcode a username and password. Take input from user. If both match print Access granted. If wrong print Access denied. Give only 3 attempts, then lock out.
correct_username = "admin"
correct_password = "cyber123"

attempts = 3

while attempts > 0:

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Access granted")
        break

    else:
        attempts = attempts - 1
        print("Access denied")

        if attempts > 0:
            print("Attempts left:", attempts)

        else:
            print("Account locked")
