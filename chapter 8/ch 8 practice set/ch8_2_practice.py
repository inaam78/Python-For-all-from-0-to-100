# Function to convert Celsius to Fahrenheit by returning the value
def celsius (c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit
result = celsius(37)
print(f"Fahrenheit is {result}")
# Function to convert Celsius to Fahrenheit taking user input
def celsius_to_fahrenheit(c):
    fahrenheit= (c * 9/5) + 32
    return fahrenheit
c=float(input("Enter temperature in Celsius: "))
result=celsius_to_fahrenheit(c)
print(f"{c}°C is {result}°F")