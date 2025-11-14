"""weather_advice program is created to provide clothing recommendations for users based on weather conditions.
 Input examples: rainy, sunny etc."""
# clothing recommendations
sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
snowy = "Make sure to wear a warm coat and a scarf."
windy = "Wear a windbreaker or a hoodie"
cloudy = "Wear a light long-sleeve shirt"
# user guide
print("Choose weather condition by number(1-5)")    
print("1. sunny\n"
      "2. rainy\n"
      "3. snowy\n"
      "4. windy\n"
      "5. cloudy")
# error handling
try:
    weather_today = int(input("What's the weather like today?: "))
    
    if weather_today == 1:
        print(sunny)
    elif weather_today == 2:
        print(rainy)
    elif weather_today == 3:
        print(snowy)
    elif weather_today == 4:
        print(windy)
    elif weather_today == 5:
        print(cloudy)
    else:
        print("Sorry, I don't have recommendations for this weather.")
        print("Please enter a number between 1 and 5.")

except ValueError:
    print("Invalid input. Please enter a number.")