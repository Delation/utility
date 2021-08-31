n = input("Your number >>> ")
try:
  n = int(n)
except:
  quit("Please enter an integer.")
for i in range(n + 1):
  if i == 0:
    continue
  if n % i == 0:
    print(f"{n} is divisble by {i}!")
