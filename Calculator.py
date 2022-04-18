# # calculator module with user input
# add
def add(x,y):
	return ( x + y)
	
# sub
def sub(x,y):
	return(x - y)
	
# mul
def mul(x,y):
	return (x * y)
	
# div
def div(x,y):
	return(x / y)
	
# Switch function
while True:
	print("Select the options: \n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division")
	r = input("Enter the desired option (1/2/3/4) : ")
	if r in ('1', '2', '3', '4'):
		num1 = float(input("Enter 1st Number: "))
		num2 = float(input("Enter 2nd Number: "))
		
		if (r == "1"):
				print(num1 , "+" , num2 , "=" , add(num1,num2))
		elif (r == "2"):
				print(num1 , "-" , num2 , "=" , sub(num1,num2))
		elif (r == "3"):
				print(num1 , "*" , num2 , "=" , mul(num1,num2))
		elif (r == "4"):
				print(num1 , "/" , num2 , "=" , div(num1,num2))
			# break loop
	next_1 = input("Press ENTER to continue / Q to quit \n")
	if (next_1 == "Q"):
		break
		
