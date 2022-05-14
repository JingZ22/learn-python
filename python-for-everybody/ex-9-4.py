name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    counts[words[1]] = counts.get(words[1],0) + 1

bigcount = None
bigname = None
for name,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        bigname = name

print(bigname, bigcount)
