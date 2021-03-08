def FizzBuzzfunc(top):
	my_str = ""
	for x in range(1, top):
		if x % 3 == 0 and x % 5 == 0:
			my_str += "FizzBuzz"
		else:
			my_str += str(x)
	return my_str