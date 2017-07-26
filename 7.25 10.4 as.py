name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours=list()
for line in handle:
	line=line.strip()
	if line.startswith("From "):
		words=line.split()
		hourraw=words[5]
		hour=hourraw[:2]
		hours.append(hour)

counts=dict()
for hour in hours:
	counts[hour]=counts.get(hour,0)+1
	
#print counts
hourlist=counts.items()
hourlist.sort()

for k,v in hourlist:
	print (k,v)