name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
fromlist=list()
for line in handle:
	line=line.strip()
	if line.startswith("From "):
		words=line.split()
		email=words[1]
		fromlist.append(email)
counts=dict()
for email in fromlist:
	counts[email]=counts.get(email,0)+1

bigcount=None
bigemail=None
for email,count in counts.items():
	if bigcount is None or count>bigcount:
		bigemail=email
		bigcount=count

print (bigemail,bigcount)