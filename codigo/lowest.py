num1 = int(input("Enter the 1º number:"))
num2 = int(input("Enter the 2º number:"))

if num1 <= num2:
    lowest = num1
else:
    lowest = num2

print("The lowest number is: " + str(lowest))
