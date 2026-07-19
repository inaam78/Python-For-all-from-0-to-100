name = "inaam"
print (name[0:4])
print(name[-4:-1]) #for negative slicing we convert negative indexes into corresponding positive indexes  (Trick)
print(name[1:4])
print (name[:4]) # is same as print (name[0:4]) it will print from start to index 4
print (name[1:]) # is same as print (name[1:5]) # it will print from index 1 to end of string
print (name[1:5]) # is same as print (name[1:])

#string slicing with skip value

a = ["inaam", "ali", "ahmed", "saad"]
print (a[1:3:1])
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a[0:15:3]) # it will print from index 0 to 14 with skip value of 3