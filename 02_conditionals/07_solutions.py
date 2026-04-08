order_size = "Medium"
extra_shots = True

if extra_shots:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + "coffee"
print(coffee)