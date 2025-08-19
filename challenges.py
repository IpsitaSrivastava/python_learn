# check if username is not empty and the age is greater than or equal to 18
username="ola"
age=18
print(bool(username) and age>=18)

# check if the password is 8 chars long & does not contain spaces
password="qwerty123"
print((len(password) > 8) and " " not in password)

# check if a user's email in not empty, contains '@' and ends with '.com'
email = "abc@xyz.com"
print(email != "" and "@" in email and email.endswith(".com") and " " not in email)

# check is username is a string, is not none, and is no longer than 5 chars
username="qwert"
print(isinstance(username, str) and username is not None and len(username) <= 5)

# check if the user is either admin or moderator and either they're not banned or 
# they've verified
is_admin= False
is_moderator= True
is_banned= True
is_verified= False

print ((is_admin or is_moderator) and ((not is_banned) or is_verified))

print ("morning")