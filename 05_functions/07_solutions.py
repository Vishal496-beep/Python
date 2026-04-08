#*args is used in parameters to store multiple values (*) is important we can use *chai too 
# sum is also a method

def sum_all(*args):
    print(args)  #its giving tuple
    for i in args:
        print(i*2)
    return sum(args)  # we can use this sum or we can use loop like shown in up

print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 6, 8, 9))