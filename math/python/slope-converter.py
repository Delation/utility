def main():
  print("CONVERT STANDARD FORM TO SLOPE-INTERCEPT FORM")
  print("Please enter the components of your standard form equation.")
  a = input("A >>> ")
  b = input("B >>> ")
  c = input("C >>> ")
  try:
    a = int(a)
    b = int(b)
    c = int(c)
  except:
    print("Numbers, please!")
    return
  
  answer = input(f"Is this the correct standard form equation? {a}x + {b}y = {c} >>> ").lower()
  if not answer.startswith("yes"):
    return
  a = a * -1
  print(f"Step 1: {b}y = {a}x + {c}")
  if a % b != 0:
    if a < 0 and b < 0:
      a = f"{a * -1}/{b * -1}"
     else:
      a = f"{a}/{b}"
  else:
    a = a / b
  if c % b != 0:
    if c < 0 and b < 0:
      c = f"{c * -1}/{b * -1}"
    else:
      c = f"{c}/{b}"
  else:
    c = c / b
  print(f"Step 2: y = {a}x + {c}")
  print("--------------------------")
  print(f"y = {a}x + {c}")

main()
