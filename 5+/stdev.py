# You might need this to calculate a square root using math.sqrt
import math

num = int(input("Enter a number (-1 to exit) "))
num_sum, count, current_average, standard_deviation = 0, 0, 0, 0

# Loop until the user types in -1
while num != -1:
    num_sum += num
    count += 1
    previous_average = current_average
    previous_standard_deviation = standard_deviation

    # Calculate the cumulative moving average and standard deviation
    current_average = previous_average + ((num - previous_average) / count)
    if count == 1:
        standard_deviation = math.sqrt(math.pow(num - current_average, 2) / count)
    else:
        standard_deviation = math.sqrt(((count * current_average) - previous_average) / count)
    print(round(standard_deviation, 2))


    standard_deviation = (previous_standard_deviation + (num - previous_average) * (num - current_average)) / count

    # Print them out within the loop
    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))

    num = int(input("Enter a number (-1 to exit) "))
