def factorial_num(n):
     if n == 0:
          return 1
     else:
         return n * factorial_num(n-1)
     
print(factorial_num(54))