import re

"""pattern = re.compile("Search this inside of this text please!")
string = "Search this inside of this text please! Hey!"

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(c)"""

# 194. Password checker
# At least 8 char long
# Contain any sort of letters, numbers and $%#@

pattern = re.compile(r"^[a-zA-Z0-9$%#@]{7,}\d$") # regex pattern to check
password = "Playabl8" 

pw_checker = pattern.fullmatch(password) 
print(pw_checker)