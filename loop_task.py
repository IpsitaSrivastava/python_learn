#Skip weekends in calendar loop
##days = ['Mon', 'Sun', 'Wed', 'Tue', 'Thu', 'Sat', 'Fri']
#weekends = ['Sat', 'Sun']
#for day in days:
#    if day in weekends:
#        continue
#    print(f'Workday: {day}')

# Scan emails to block unsafe data from entering system
emails = [
    'data@gmail.com',
    'ipsi@outlook.com',
    'DROP TABLE USERS;',
    'maria@hotmail.com',
]
for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f"Processing Email: {email}")