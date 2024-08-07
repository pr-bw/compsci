# int
x = 24
print("data:", x, ", tipe data:", type(x))

# float
y = 1.5
print("data:", y, ", tipe data:", type(y))

# str
catName = "Titi"
print("data:", catName, ", tipe data:", type(catName))

# bool
isPrabowoHandsome = True
print("data:", isPrabowoHandsome, ", tipe data:", type(isPrabowoHandsome))

# complex
complex_number = complex(10, 5)
print("data:", complex_number, ", tipe data:", type(complex_number))

# from ctypes

import ctypes

from ctypes import c_float

pi = c_float(3.14)
print("data: ", pi, "tipe data: ", type(pi))