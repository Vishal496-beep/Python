username = "vishal"

def fnc():
    # username = "chai"
    print(username)

print(username)
fnc()

x = 99
# def func(y):
#     z = x + y
#     return z

# result = func(1)
# print(result)

# def func1():
#     global x #avaid using global
#     x = 12

# func1()
# print(x)

# global inside fnc it means we are changing values of global variables inside function also we should not use it 

def func2():
    x = 88
    def fn3():
       print(x)
    return fn3
myRes = func2()
myRes()
# func2 is a closure means it will not only print fn3 but whatever the reference fn3 hava also we can call it backpacking



def chaiaurcode(num):
    def actual(x):
        return x ** num
    return actual
f = chaiaurcode(2)
g = chaiaurcode(3)
print(f)