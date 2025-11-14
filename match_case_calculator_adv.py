# Simple Calculator

# function that accepts first and second number from user
def ask_user():
    num1 = float(input("1-> "))
    num2 = float(input("2-> "))
    operator(num1, num2)
    
# function that adds two numbers
def addition(first_num, second_num):# +
    answer = first_num + second_num
    return answer
    
# function that subtracts two numbers
def subtraction(first_num, second_num):# -
    answer = first_num - second_num
    return answer
    
# function that multiplies two numbers
def multiplication(first_num, second_num):# *
    answer = first_num * second_num
    return answer
    
# function that divides two numbers
def division(first_num, second_num):# /
    answer = first_num / second_num
    return answer

# function that accepts operator sign from user   
def operator(first_num, second_num):
    op = input("operator: ")
    match op:
        case "+":
            print(f"Result: {addition(first_num, second_num):.2f}")
        case "-":
            print(f"Result: {subtraction(first_num, second_num):.2f}")
        case "*":
            print(f"Result: {multiplication(first_num, second_num):.2f}")
        case "/":
            print(f"Result: {division(first_num, second_num):.2f}")
        case _:
            print("Invalid input!")
    
ask_user()