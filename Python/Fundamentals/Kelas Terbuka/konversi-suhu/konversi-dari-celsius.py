# Konversi dari Celsius
celsius = float(input("Masukkan suhu dalam Celsius: "))
print("Suhu dalam Celsius:", celsius, "°C")

celsius_to_reamur = celsius * (4 / 5)
print("Suhu dalam Reaumur:", round(celsius_to_reamur, 2), "°R")

celsius_to_kelvin = celsius + 273.15
print("Suhu dalam Kelvin:", round(celsius_to_kelvin, 2), "K")

celsius_to_fahrenheit = (celsius * (9/5)) + 32
print("Suhu dalam Fahrenheit:", round(celsius_to_fahrenheit, 2), "°F")