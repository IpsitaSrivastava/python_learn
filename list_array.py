x = [9, 12, 7, 4, 11]

# Add element:
x.append(8)

# Sort list ascending:
x.sort()

print(x)

# Creating an algorithm to find lowest value in a list
mylist = [11, 7, 10, 3, 9, 6, 50]
mylist.sort()
minVal = mylist[0]
for i in mylist:
    if i<minVal:
        minVal=i
print("Lowest Value Is: ", minVal)