#   FOR LOOP
items = 1,2,3,4,5,"Over"
for item in items:
    print(f"Round: {item}")

#for item in range (start,stop,step):
for item in range (2, 12, 2):
    print(f"Round: {item}")

# Aggregation - list of scores
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total = total + score
    print("Current Total:", total)
print("Final Total", total)

# loops to transform data
files = [' Report.csv', 'DATA.csv ', 'final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")

# Print 7-times table from 1 to 10
# using a loop
table = 7
for table in range (1, 11):
    print(f"7 X {table} =", table*7)

# Print a left aligned pyramid
# of stars with 6 rows
i = "*"
for i in range (1,7):
    print("*"*i)