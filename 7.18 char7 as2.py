fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
a = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") :
		 continue
	cnt = cnt + 1
	a = a + float(line.split(':')[1].lstrip())
print ("Average spam confidence:", a / cnt)

