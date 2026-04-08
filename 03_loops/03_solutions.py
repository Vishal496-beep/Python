n = int(input("Enter a table no.  "))

for i in range(1, 11):
    if i == 5:
        continue
    print(n, "X", i, "=",n*i)