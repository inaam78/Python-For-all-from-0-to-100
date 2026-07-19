marks_1=int(input("enter marks  of chemistry: "))
marks_2=int(input("enter marks  of physics: "))
marks_3=int(input("enter marks  of maths: "))
total_percentage=(100*(marks_1+marks_2+marks_3))/300 
if(total_percentage>=40 and marks_1>=33 and marks_2>=33 and marks_3>=33):   
#   AND operation combines conditions and gives True only if all conditions are True.
    print("you are pass with percentage : ",total_percentage)
else:
    print("you are fail with percentage : ",total_percentage)