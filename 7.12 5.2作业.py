largest = None  
smallest = None  
  
while True:  
	num = input("Enter a number: ")  
	if num == "done" : break  
		  
	try:  
		n=int(num)  
  
	except:  
		print ("Invalid input" ) 
			  
	if n>largest:  
		largest=n  
	if smallest is None or n<smallest:  
		smallest=n  
	#elif n<smallest:  
		#smallest=n  
  
	  
print ("Maximum is", largest)  
print ("Minimum is", smallest)