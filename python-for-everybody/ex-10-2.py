name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle :
    line = line.rstrip()
    words = line.split()
    if len(words) < 6 or words[0] != 'From' : continue
    #print(line)
    time = words[5]
    #print(time)
    time_split = time.split(":")
    hour = time_split[0]
    counts[hour] = counts.get(hour,0) + 1
#print(counts.items())
for key,value in sorted(counts.items()) :
    print(key,value)
