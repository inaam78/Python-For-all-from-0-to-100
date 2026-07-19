day = 10

match day:
    case 1:
        print("Monday")

    case _:
        print("Invalid")
# ye dosri langauage me jaisa switch case hota hai, python me match case hota hai. 
fruit = "apple"

match fruit:
    case "apple":
        print("Red Fruit")

    case "banana":
        print("Yellow Fruit")
    case _:
        # ye case _ else ki tarah hai, agar upar ke cases match nahi karte to ye case execute hoga.
        print("Unknown Fruit")


1