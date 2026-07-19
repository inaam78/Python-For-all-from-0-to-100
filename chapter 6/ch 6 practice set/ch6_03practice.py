p1="subscribe"
p2="buy now"
p3="click here"
p4="make free money"
p5="free gift"
message=input("enter your comment:" )
if((p1 in message)or(p2 in message)or(p3 in message)or(p4 in message)or(p5 in message)):   
#  OR operation   Combines multiple conditions.
# If any one condition is True, the whole statement is True.
    print("spam")
else:
    print("not spam")
    