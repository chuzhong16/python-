import os

path = os.path.expanduser(r"/Users/mac/Desktop/haha .txt")
print(path)
with open(path) as f:
	content = f.read()
	for i in content.splitlines():
		print i