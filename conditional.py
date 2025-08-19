#   if, elif, else,
#   nested ifs, independant ifs
score = 95
project = True
if score >= 90:
    if project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")