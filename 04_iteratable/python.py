import time

username = "vishal"
print(username)

age = 22

# readline
# open() only for files otherwise for lists iter()

f = open('python.py') 
while True:
    line = f.readline()
    if not line: break
    print(line, end='')