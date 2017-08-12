import re
hand=open('mbox-short.txt')
for line in hand:
	line=line.rstrip()
	x=re.findall('^x\S:',line)
	if len(x)>0:
		print(x)