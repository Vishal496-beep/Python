distance = 24

if distance < 3:
    transportation = "Go by walking"
elif distance <= 15:
    transportation = "Get a bike"
else:
    transportation = "Go by car"

print(transportation)