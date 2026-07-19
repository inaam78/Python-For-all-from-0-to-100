def inches_to_cm(inches):
  centimeters = inches*2.54
  return centimeters
inch = float(input("Enter length in inches: "))
result=inches_to_cm(inch)
print(f"inches is {result} centimeters")


