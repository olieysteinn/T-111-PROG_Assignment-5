# 1. A user inputs a number
# 2. The user inputs another number
# 3. The numbers are compared and the bigger number is saved into a variable
# 4. Repeat steps 2 and 3 until the user inputs a negative number
# 5. Print out the maximum number

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0
while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
