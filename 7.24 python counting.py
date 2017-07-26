counts=dict()
names=['csev','cwen','csev','qzuar']
for name in names:
	if name not in counts:
		counts[name]=1
	else:
		counts[name]=counts[name]+1
print(counts)

counts=dict()
names=['csev','cwen','cseb','cwen','csev']
for name in names:
	counts[name]=counts.get(name,0)+1
print(counts)




