def num_str(func,seq):
	return[fun(i) for i in seq]
def foo():
	def bar():
		print("bar is running")
	bar()
	print("foo is running")
foo()
def haha():
	def bar():
		print("bar is running")
	return bar
haha()
foo()