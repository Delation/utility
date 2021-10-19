# Fun little program~!
def check(n:int):
	try:
		n = int(n)
	except:
		raise Exception("Needs to be an integer!")
	if "13" not in str(n):
		return False
	if str(bin(n)).count('1') % 2 != 0:
		return False
	return True
	
def main():
	n = 0
	f = 1000000
	for i in range(f):
		if check(i):
			print(i,bin(i))
			n += 1
	print(f"Went through {f} iterations (0-{f-1}) and found {n} valid matches.")

main()
