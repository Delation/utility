# Crappy factoring calculator!
def factor(multiply:int,add:int):
	for i in range(abs(multiply)*2+1):
		i = i - 5
		for n in range(abs(add)*2+1):
			n = n - 5
			if i * n == multiply and i + n == add:
				return i,n

def main():
	a = int(input('ax²: '))
	b = int(input('bx: '))
	c = int(input('c: '))
	d = factor(a*c,b)
	op1 = '+'
	op2 = '+'
	if d[0] < 0:
		op1 = '-'
	if d[1] < 0:
		op2 = '-'
	print(f"Original equation: {a}x² + {b}x + {c}\nAnswer: (x {op1} {abs(d[0])})(x {op2} {abs(d[1])}) = 0\nx can be equal to either {d[0]*-1} or {d[1]*-1}!")

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(e)
