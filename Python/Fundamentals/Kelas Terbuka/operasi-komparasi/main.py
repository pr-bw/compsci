x = 5 # assignment untuk membuat object
y = 2
z = 2

# A.) Komparasi Lebih Sesuai Digunakan Untuk Nilai Literal

# 1. less than (<)
hasil = x < 10 # di sini 10 merupakan nilai literal karena tidak hidup dalam variable (object)
print(x, "<", 10, "=", hasil)

print("==========")

# 2. greater than (>)
hasil = x > y
print(x, ">", y, "=", hasil)

print("==========")

# 3. less than or equal to (<=)
hasil = y <= z
print(y, "<=", z, "=", hasil)

print("==========")

# 4. greater than or equal to (>=)
hasil = y >= z
print(y, ">=", z, "=", hasil)

print("==========")

# 5. equal to (==)
hasil = y == 2
print(y, "==", 2, "=", hasil)

print("==========")

# 6. not equal to (!=)
hasil = y != 2
print(y, "!=", 2, "=", hasil)

print("\n==========\n")

# B.) Komparasi Lebih Sesuai Digunakan Untuk Komparasi Object Identity
x = 2
y = 2
z = 20
"""
walau variable x dan y berbeda, jika ada nilai yang sama khususnya untuk nilai berupa angka, maka python secara pintar melakukan pengalamatan ke alamat memori yang sama untuk variable-variable yang memiliki nilai yang sama.
"""

print(hex(id(x)))
print(hex(id(y)))

# 1.) is
print(x is y)
print(x is not y)

# 2.) is not
print(x is z)
print(x is not z)