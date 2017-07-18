fname=input('Enter the file name: ')
try:
	fhand=open(fname)
except:
	print('File cannot be opened:',fname)
	quit()
	
count=0
for shigefei in fhand:
	if shigefei.startswith('Subject: '):
		count=count+1
print('There were',count,'subject lines in',fname)