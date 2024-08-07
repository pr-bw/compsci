# Konversi dari Kelvin
kelvin = float(input("Masukkan suhu dalam Kelvin: "))
print("Suhu dalam Kelvin:", kelvin, "K")

kelvin_to_celsius = kelvin - 273.15
print("Suhu dalam Celsius:", round(kelvin_to_celsius, 2), "°C")

kelvin_to_reamur = (kelvin - 273.15) * (4/5)
print("Suhu dalam Reaumur:", round(kelvin_to_reamur, 2), "°R")

kelvin_to_fahrenheit = ((kelvin - 273.15) * (9/5)) + 32
print("Suhu dalam Fahrenheit:", round(kelvin_to_fahrenheit, 2), "°F")