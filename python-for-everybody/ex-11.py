import re

name = input("Enter file:")
handle = open(name)
file = handle.read()
numbers = re.findall('[0-9]+',file)
total = 0
for number in numbers :
    total = total + int(number)
print(total)
