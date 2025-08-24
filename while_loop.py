# While Condition
#answer = ""
#while answer != "yes":
#    answer = input("Do you agree?: ")
#print("Thanks!")

# While True
# 3 attempts
attempts = 0
while attempts < 3:
    answer = input("Do you agree?: ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 Strikes! You're Out")