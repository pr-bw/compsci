# int

# x = 2
x = 0

var_float = float(x)
var_str = str(x)
var_bool = bool(x)

print(var_float, "data type:", type(var_float))
print(var_str, "data type:", type(var_str))
print(var_bool, "data type:", type(var_bool))

print("===========================")

# x = 2.25
x = 0

var_int = int(x)
var_str = str(x)
var_bool = bool(x)

print(var_int, "data type:", type(var_int))
print(var_str, "data type:", type(var_str))
print(var_bool, "data type:", type(var_bool))

print("===========================")

var_str = "mouse"

# var_int = int(var_str) ERROR
# var_float = float(var_str) ERROR
var_bool = bool(var_str)

# print(var_int, "data type:", type(var_int))
# print(var_float, "data type:", type(var_float)) ERROR
print(var_bool, "data type:", type(var_bool))

print("===========================")

var_bool = False

var_int = int(var_bool)
var_str = str(var_bool)
var_float = float(var_bool)

print(var_int)
print(var_str)
print(var_float)