# for i in range(1,6,):
#  for j in range(1,6):
#     print(i)
# n=5
# for j in range(n):
#     print("*",end=" ")#end is used to print the stars in same line
# n=5
# for i in range(n):
#  for j in range(n):
#   print("*",end=" ")
#  print()#if no indented(spaces or tabs) then the loop is probably ended
#simple right angle triangle
# n=5
# for i in range(n):
#  for j in range(i+1):
#   print("*",end=" ")
#  print()
#reverse triangle
# size = 5  # Define the size of the triangle
# for i in range(size, 0, -1):  # Outer loop: starts from size, decreases to 1
#     for j in range(i):  # Inner loop: prints '*' i times
#         print("*", end=" ")
#     print()  # Moves to the next line after each row
# n=5
# for i in range(n):
#   for j in range(i,n):
#    print(" ",end="")
#   for j in range(i+1):
#    print("*",end="")
#   print()
#right side triangle
# n=5
# for i in range(n):#loop for controlling number of rows
#     for j in range(i+1):#loop for spaces increasing or decreasing
#      print(" ",end="")
#     for j in range(i,n):#loop for printing stars in current row
#      print("*",end="")
#     print()
#hill pattern below
# size = 5  # Define the height of the hill
# for i in range(1, size + 1):  # Loop for rows (1 to size)
#     for j in range(size - i):  # Loop for leading spaces (decreasing)
#         print(" ", end="")
#     for k in range(2 * i - 1):  # Loop for printing stars (odd count)
#         print("*", end="")
#     print()  # Move to the next line
#reverse hill pattern
size=5
for i in range(size,0,-1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()




