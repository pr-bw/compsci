x = 11
y = 7

print("Bitwise dari", x, "=\t", format(x,'08b'))
print("Bitwise dari", y, "=\t", format(y, '08b'))

print("\n==========\n")

# 1.) bitwise or
hasil = x | y
print("Hasil bitwise or", hasil, "=\t", format(hasil, '08b'))

# 2.) bitwise and
hasil = x & y
print("Hasil bitwise and", hasil, "=\t", format(hasil, '08b'))

# 3.) bitwise xor
hasil = x ^ y
print("Hasil bitwise xor", hasil, "=\t", format(hasil, '08b'))

# 4.) bitwise not
hasil = ~ x
print("Hasil bitwise not dari", x, "=", format(hasil & 0xFF, '08b'))