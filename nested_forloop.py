colors = ['red', 'blue', 'yellow'] #outer loop
sizes = ['S', 'M', 'L'] #ninner loop
for color in colors:
    for size in sizes:
        print(f"{color} - {size}")

years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1,32)

for y in years:
    for m in months:
        for d in days:
            print(f"report.csv{d}/{m}/{y}")

