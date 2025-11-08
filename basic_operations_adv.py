# Program that finds the addition, subtraction and multiplication of two numbers
number_1 = 20 # first number
number_2 = 10 # second number

addition = number_1 + number_2

subtraction = number_1 - number_2

multiplication = number_1 * number_2

var_name = (
    ["addition", addition],
    ["subtraction", subtraction],
    ["multiplication", multiplication]
)

for i,j in var_name:
    print(f"{i} of {number_1} and {number_2} is {j}")