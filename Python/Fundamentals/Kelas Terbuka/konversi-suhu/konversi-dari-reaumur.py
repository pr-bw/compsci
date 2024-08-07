# Konversi dari Reaumur
reaumur = float(input("Masukkan suhu dalam Reaumur: "))
print("Suhu dalam Reaumur:", reaumur, "°R")

reaumur_to_celsius = reaumur * (5 / 4)
print("Suhu dalam Celsius:", round(reaumur_to_celsius, 2), "°C")

reaumur_to_kelvin = (reaumur * (5/4)) + 273.15
print("Suhu dalam Kelvin:", round(reaumur_to_kelvin, 2), "K")

reaumur_to_fahrenheit = (reaumur * (9/4)) + 32
print("Suhu dalam Fahrenheit:", round(reaumur_to_fahrenheit, 2), "°F")