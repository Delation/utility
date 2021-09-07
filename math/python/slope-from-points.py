def main():
	x1 = input("x1 >>> ")
	y1 = input("y1 >>> ")
	
	x2 = input("x2 >>> ")
	y2 = input("y2 >>> ")
	
	try:
		x1 = int(x1)
		y1 = int(y1)
		x2 = int(x2)
		y2 = int(y2)
	except:
		print("Numbers, please!")
		return
	
	a = x1 - x2
	b = y1 - y2
	if b % a == 0:
		c = b / a
	else:
		c = f"{b}/{a}"
	
	d = f"{y1 - (x1 * (b / a))}"
	print("-----------------------")
	print(f"Slope: {c}\n"
	f"Intercept: {d}\n"
	f"Equation: y = {c}x + {d}")
	
main()
