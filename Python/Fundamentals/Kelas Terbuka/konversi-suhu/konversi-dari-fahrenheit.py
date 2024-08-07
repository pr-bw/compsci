# Konversi dari Fahrenheit
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
print("Suhu dalam Fahrenheit:", fahrenheit, "°F")

fahrenheit_to_celsius = (fahrenheit - 32) * (5/9)
print("Suhu dalam Celsius:", round(fahrenheit_to_celsius, 2), "°C")

fahrenheit_to_reamur = (fahrenheit - 32) * (4/9)
print("Suhu dalam Reaumur:", round(fahrenheit_to_reamur, 2), "°R")

fahrenheit_to_kelvin = ((fahrenheit - 32) * (5/9)) + 273.15
print("Suhu dalam Kelvin:", round(fahrenheit_to_kelvin, 2), "K")
