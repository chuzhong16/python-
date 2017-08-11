import re
x='From: using the : character123:'
y=re.findall('^F.+:',x)
print(y)