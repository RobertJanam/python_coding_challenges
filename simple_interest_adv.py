# Program that calculates the simple interest based on user's given principal amount, rate of interest, and time.

principal = float(input("Enter principal amount (eg. 1000): "))

rate = float(input("Enter rate in percentage (eg. 5): "))

# choose whether you want to enter time in years or months
choice_of_time = input("Choose time selection (months or years) [m/Y]:").lower()

time = float(input("Enter time: "))

time = (time / 12.0) if choice_of_time == "m" else time # sets default time selection to years.
rate = rate / 100 # converts percentage rate for easy calculation
interest = principal * rate * time # formula

print(f"\nThe simple interest is: {interest}")