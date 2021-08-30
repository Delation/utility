# This is supposed to calculate a list of prime numbers
# but it turns out there isn't a consistent formula for finding new ones
# so this script is broken

def check_prime(n:int):
	for i in range(n + 1):
		if i == 0:
			continue
		if n % i == 0:
			if i not in (1,n):
				return False
	return True

def new_prime(n:int,xrange:int):
	list = []
	x = n
	for i in range(xrange):
		x = 6*x+1
		list.append(x)
	x = n
	for i in range(xrange):
		x = 6*x-1
		list.append(x)
	return list

def find_percentage(xrange:int):
	list = []
	for i in range(39):
		i += 1
		n = i*i+i+41
		list.append(check_prime(n))
		for item in new_prime(n,xrange):
			list.append(check_prime(item))
	return list.count(True) / len(list) * 100
	
def main():
	print(f"The formula gets a prime number {find_percentage(5)}% of the time.")

if __name__ == "__main__":
    main()
