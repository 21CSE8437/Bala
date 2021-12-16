while 0==0:
	name = (input("Enter your name - "))
	engmark = int(input("Enter English Mark - "))
	matmark = int(input("Enter Maths Mark - "))
	phymark = int(input("Enter physics Mark - "))
	chemmark = int(input("Enter Chemistry Mark - "))
	pytmark = int(input("Enter Python mark - "))
	total = engmark+matmark+phymark+chemmark+pytmark
	print("Your Total is ",total)
	avg = total/5
	print('Your Average is ',avg)
