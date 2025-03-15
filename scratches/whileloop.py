# a=10
# while a<=20:
#   print("Abdullah Amjad")
#   a=a+1
# print(a)#this print statement marks the end of while loop thus the value is 21
# b=10
# while b>=1:
#     print("Python")
#     b=b-1
# print(b)
# # #while loop program print num from 1 to 10
# num=1
# while num<=10:
#     print(num)
#     num+=1#another way num=num+1
# print()
# #sum of first n natural numbers
# num1=int(input("Enter number of natural numbers:"))
# sum=0
# i=1
# while i<=num1:
#   sum+=i
#   i+=1
# print("sum of n natural number is:",sum)
#reverse counting from 10 to 1
# i=10
# while i>=1:
#     print(i)
#     i-=1
# print()
# print even numbers upto n
# n=int(input("Enter the number of terms:"))
# i=2
# while i<=n:
#     print(i)
#     i+=2
# print()
#multiplication table of a number
# num=int(input("Enter a number"))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i=i+1
# print()
#reverse a number
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10#modulus operator extract the last digit and store it in rev variable
#     num //= 10#floor division remove the last digit of the num variable
# print("Reversed Number:", rev)#at last after condition become false print the reversed number
#count digits in a number
# num=int(input("Enter a number"))
# count=0
# while num>0:
#     num//=10
#     count+=1
# print("The number of digits in the given number is",43567,"=",count)
#sum of digits of a number
# num=int(input("Enter a number:"))
# sumdigits=0
# while num>0:
#     sumdigits+=num%10
#     num//=10
# print("The sum of digits of a number are:",sumdigits)
#factorial of a number
# num=int(input("Enter a number:"))
# factorial=1
# while num>0:
#     factorial*=num
#     num-=1
# print("factorial of a number is","=",factorial)
#check if a num is palindrome
num = int(input("Enter a number: "))
original = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if original == rev:
    print("Palindrome")
else:
    print("Not a palindrome")