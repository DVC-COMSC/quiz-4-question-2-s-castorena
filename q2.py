
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
userString = None
previous = None
larger = None
Smaller = None
while (userString != "stop") and (userString != "STOP"):
     userString = input('Enter string, enter stop when finished: ')
     if (previous is not None) and (len(userString < previous) and len(userString) < smaller):
        smaller = userString
     if (previous is not None) and (len(userString) > previous) and (len(userString) > larger):
        larger = userString 
previous = len(userString)         
print(larger, smaller)