#ASSIGMENT_05
import re

pan = input("Enter PAN number: ")

pattern = "^[A-Z]{5}[0-9]{4}[A-Z]$"

if re.match(pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")

