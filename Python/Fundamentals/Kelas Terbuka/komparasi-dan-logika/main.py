# PR

# No. 1
n = float(input("=> Masukan n: "))

is_minus = (n < 0) or (n > 5 and n<8) or (n>11)
print(n, "masih dalam rentang minus?", is_minus)

is_plus = (n >= 0 and n <= 5) or (n>=8 and n <= 11)
print(n, "masih dalam rentang plus?", is_plus)

print("\n==========\n")

# No. 2
n = float(input("=> Masukan n: "))

is_minus = (n > 0 and n <= 5) or (n>8 and n <= 11)
print(n, "masih dalam rentang minus?", is_minus)

is_plus = (n < 0) or (n > 5 and n <= 8) or (n>11)
print(n, "masih dalam rentang plus?", is_plus)


