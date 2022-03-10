def check_prime(n:int):
	return len([ i for i in range(1,n + 1) if n % i == 0 ]) == 2
	
def new_prime(n:int,xrange:int):
	list = []
	if not check_prime(n):
		return list
	x = n
	for i in range(xrange):
		x = 6*x+1
		list.append(x)
	x = n
	for i in range(xrange):
		x = 6*x-1
		list.append(x)
	return list

def find_primes(irange:int,xrange:int):
	list = []
	if irange > 40:
		irange = 40
	for i in range(irange):
		n = i*i+i+41
		list.append(n)
		list.extend(new_prime(n,xrange))
	return [ i for i in list if check_prime(i) ]

def main():
	recursion_depth = 1
	list = find_primes(40,recursion_depth)
	print(f"The formula has found {len(list)} prime numbers with a recursion depth of {recursion_depth}.")

if __name__ == "__main__":
    main()
