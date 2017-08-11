import re
s='Hello from csev@umich.edu to cwen@inpui.edu about the meeting @2PM'
lst=re.findall('\S+@\S+',s)
print(lst)