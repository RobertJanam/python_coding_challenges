# Program that calculates the area of a rectangle using its length and width.
while True:
    try:
        length = int(input("Enter Length: "))
        width = int(input("Enter Width: "))
        
        area = length * width
        
        print(f"area = {length} * {width}")
        print(f"The area of the rectangle is: {area}")
        break
        
    except ValueError:
        print("Invalid input! Please enter integer values only.")