def greet(name="Guest"):
    print("Hello", name)

greet()          # koi argument nahi diya
greet("Hassan")  # argument diya


# Function with default argument
def greet(name ="stranger",greeting="Thank you"):
    print( "Good day "+name)
    print(greeting)
greet("inaam")
greet("inaam","Good day")
