#1.	Greeting
name = input ("Enter Your Name:")
print("Hello",name)



#2.	Sum of 2 numbers
a1 = int (input ("enter num1:"))
a2 = int (input ("enter num2:"))
print ("sum:", a1+a2 )



#3.	Age check
age = int (input("enter age:"))
if age>=18:
    print("you are a adult")
else:
    print("you are not a adult chotuu")



#4.	Calculator (+, -, *, / with zero check)
num1 = int (input("enter number 1:"))
num2 = int (input("enter number 2:"))

op = input("(+, -, *, /):")

if op == "+":
    print("SUM:", num1 + num2)
elif op == "-":
    print("SUBTRACTION:", num1-num2 )
elif op== "*":
    print("PRODUCT:", num1*num2 )
elif op == "/":
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        print("DIVIDE:", num1 / num2)
else:
    print ("SELECT APPROPIATE OPERATOR")


#5.	Even/Odd
num3 = int (input("ENTER NUM:"))
if num3%2 ==0 :
    print("EVEN")
else:
    print("ODD")


#6.	Largest of 3 numbers
a1 = int (input("ENTER NUM1:"))
a2 = int (input("ENTER NUM2:"))
a3 = int (input("ENTER NUM3:"))
print("IS LARGEST", max(a1,a2,a3))


#7.	Reverse a number
num = input("Enter number: ")
print(num[::-1])