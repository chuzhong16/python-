def foo(x,y,z,*args,**kargs):
	print(x)
	print(y)
	print(z)
	print(args)
	print(kargs)
foo(1,2,3)
foo(1,2,3,4,5,6)
foo(1,2,3,4,5,6,a=7,b=8,c=9)
