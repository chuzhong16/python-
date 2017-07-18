def foo(fun):
	def wrap():
		print("start")
		fun()
		print("end")
		print(fun.name)
	return wrap

def bar():
	print("haha")
bar()