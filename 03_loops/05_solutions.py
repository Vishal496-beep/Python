input_str = "teteer"

for char in input_str:
    if input_str.count(char) == 1:
        print("first non repeating char is ", char)
        break