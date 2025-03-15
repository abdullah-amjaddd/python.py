def factorial(n):
    fact = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        fact *= i  # Multiply fact by i
    return fact#the function is returning the final value of fact to main and main prints it
#output
# 1st iteration fact*=1 1 is stored in fact variable
# 2nd iteration fact*=2 2 is multiplied with fact whose value is 1
# 3rd iteration fact*=3 3 is multiplied with fact whose value is 2 so now fact is 6
# 4th iteration fact*=4 4 is multiplied with fact whose value is 6 so now fact is 24
# 5th iteration fact*=5 5 is multiplied with fact whose value is 25 so final ans will be 120
num = int(input("Enter a number: "))  # Take user input
print("Factorial of", num, "is", factorial(num))  # Call the function and print result
