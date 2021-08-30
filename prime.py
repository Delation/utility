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

def new_prime(n:int):
	print(check_prime(6*n+1))
	print(check_prime(6*n-1))
	return [6*n+1,6*n-1]

for i in range(39):
	i += 1
	print(i)
	n = i*i+i+41
	print(check_prime(n))
	new_prime(n)
