# 1. The user inputs the length of the sequence
# 2. Run a for loop with the sequence length and add up to the first three numbers in the sequence into variables
# 3. Print out the three numbers
# 4. Put the sum of the three numbers into a variable
# 5. Set the second number as the first, the third as the second and the sum as the third
# 6. Repeat steps 3 - 5 until the secuence length has been reached

n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_sum = 0

for num in range(1, n+1):
    if num == 1:
        first_num = num
        print(num)
    elif num == 2:
        second_num = num
        print(num)
    elif num == 3:
        third_num = num
        print(num)
    else:
        num_sum = first_num + second_num + third_num
        first_num = second_num
        second_num = third_num
        third_num = num_sum
        print(num_sum)